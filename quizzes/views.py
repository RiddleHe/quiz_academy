from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Question, Quiz, Score

# Create your views here.

@login_required
def index(request):
    # pull up the user's past scores
    temp = Score.objects.filter(user=request.user).order_by('-created_time')
    if len(temp) >= 3:
        scores = temp[0:3]
    else:
        scores = temp
    # pull up the user's past quiz
    quizzes = Quiz.objects.all()
    # send context
    context = {'scores': scores, 'quizzes': quizzes}
    return render(request, 'quizzes/index.html', context)

@login_required
def quiz(request, quiz_id):
    """Load the individual quiz page and the first question"""
    quiz = Quiz.objects.get(id=quiz_id)
    scores = Score.objects.filter(quiz=quiz, user=request.user).order_by('-created_time')

    if request.method == "POST":
    # get ready to see the first question

        # pull up the first question
        questions = quiz.question_set.order_by('id')
        question_1 = questions[0]
        # create the score and save it
        score = Score()
        score.quiz = quiz
        score.user = request.user
        score.save()

        return HttpResponseRedirect(reverse('quizzes:question', args=[question_1.id]))

    # display quiz info
    context={'quiz': quiz, 'scores': scores}
    return render (request, 'quizzes/quiz.html', context)

@login_required
def question(request, question_id):
    """Load the question"""
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        # pull up the score
        scores = Score.objects.filter(user=request.user).order_by('-created_time')
        score = scores[0]
        # change the score
        score.total += 1
        if question.answer == request.POST.get("options"):
                score.score += 10
                score.correct += 1
        else:
                score.wrong += 1
        score.percentage = score.score / (score.total*10) * 100
        score.save()
        # pull up the next question
        questions = question.quiz.question_set.order_by("id")
        question_index = (*questions,).index(question)
        # check if this is the last question, if it is, to next
        if question_index + 1 < len(questions):  
            question_next = questions[question_index + 1]
            question_next_id = question_next.id

            return HttpResponseRedirect(reverse('quizzes:question', args=[question_next_id]))
        # if it's not, submit and see score
        else: 
            return HttpResponseRedirect(reverse('quizzes:result'))

        
    context = {'question': question}
    return render(request, 'quizzes/question.html', context)

@login_required
def result(request):
    """Load the result page"""
    # pull up the score
    scores = Score.objects.filter(user=request.user).order_by('-created_time')
    score = scores[0]
    context = {'score': score}
    return render(request, 'quizzes/result.html', context)
