import socket
from threading import Thread
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
server.bind((ip_address,port))
server.listen()
clients=[]
print("server is running s")

def get_random_question_answer(conn):
    random_index=random.randint(0,len(questions)-1)
    random_question=question[random_Index]
    random_answers=answers[random_index]
    conn.send(random_questions.encode(utf-8))
    return random_index, random_question, random_answers






def remove_question(index):
    questions.pop(index)
    answers.pop(index)


def clientthread (conn):
    score=0
    conn.send("Welcome to this quiz game!".encode("utf-8"))
    conn.send("you will receive a question . The answer to that question should be one of a, b,c,d")
    conn.send("Good luck! \n\n".encode(utf-8))
    index,question,answer = get_random_question_answer(conn)
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                if message .lower()==answer:
                    score+1
                    conn.send(f"Bravo!, Your score is {score}\n\n".encode("utf-8"))
                    else:
                        conn.send("Incorrect answer! Better Luck Next Time!\n\n.encode("utf-8"))
                        remove_question(index)
                        index,question,answer=get_random_question_answer(conn)
            else:
                remove(conn)
            except:
                continue
