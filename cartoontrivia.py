import flet as ft
def main(page: ft.Page):
    page.title = "Cartoon Trivia"

    question_number = 0
    score = 0
    answers = []
    questions = [
        ["Which cartoon features Finn and Jake?",
         "Adventure Time",
         "The amazing world of gumball",
         "Randy Cunningham: Ninja Total", 
         "Samurai Jack",
         "Villainous",
         "Teen Titans Go",
         "Manzana Y Cebollin",
         "Ben 10 (la primera)",
         "Looney Tunes",
         "Infinity Train",
         "Scooby Doo",
]
    ]
    def welcome(e):
        page.controls.clear()
        title = ft.Text("Cartoon Trivia")
        start = ft.ElevatedButton("Start Quiz", on_click=show_question)
        page.add(title, start)
        page.update()
    def show_question(e):
        page.controls.clear()
        q = ft.Text(questions[question_number][0])
        option1 = ft.ElevatedButton(questions[question_number][1], on_click=answer)
        option2 = ft.ElevatedButton(questions[question_number][2], on_click=answer)
        option3 = ft.ElevatedButton(questions[question_number][3], on_click=answer)
        option4 = ft.ElevatedButton(questions[question_number][4], on_click=answer)
        next_button = ft.ElevatedButton("Next", on_click=next_question)
        page.add(q, option1, option2, option3, option4, next_button)
        page.update()
    def answer(e):
     nonlocal score
    if e.control.text == questions[question_number][5]:
        score += 1
        answers.append("correct")
    else:
        answers.append("wrong")
    def next_question(e):
        nonlocal question_number
        question_number += 1
        if question_number < len(questions):
            show_question(None)
        else:
            results(None)
    def results(e):
        page.controls.clear()
        result = ft.Text("Your score: " + str(score))
        restart = ft.ElevatedButton("Restart Quiz", on_click=restart)
        page.add(result, restart)
        page.update()
    def restart(e):
        nonlocal question_number, score
        question_number = 0
        score = 0
        welcome(None)
    welcome(None)
ft.app(target=main)  