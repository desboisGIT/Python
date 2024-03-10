import pygame
import socket
import threading

pygame.init()

width, height = 1024, 620
surface = pygame.display.set_mode((width, height))
color = (200, 200, 200)
running = True

string = ""
font = pygame.font.SysFont(None, 24)

chat = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5555))
server_socket.listen(5)

clients = []  # List to store connected clients

def handle_clients():
    global chat, clients
    while running:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)  # Add the client socket to the list
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    global chat, clients
    while running:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            chat.append(message)
            print(f"Received message: {message}")
        except Exception as e:
            print(f"Error: {e}")
            break

server_thread = threading.Thread(target=handle_clients)
server_thread.start()

while running:
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in range(pygame.K_a, pygame.K_z + 1):
                # Append the pressed letter to the string
                string += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character from the string
                string = string[:-1]
            elif event.key == pygame.K_SPACE:
                # Append a space to the string
                string += " "
            elif event.key == pygame.K_RETURN:
                chat.append(string)
                # Send the message to all connected clients
                for client_socket in clients:
                    try:
                        client_socket.send(string.encode('utf-8'))
                    except Exception as e:
                        print(f"Error sending message to client: {e}")
                string = ""

    # Display chat messages
    for pos, message in enumerate(chat):
        img = font.render(message, True, (0, 0, 0))
        surface.blit(img, (20, 20 * pos))
    img = font.render(string, True, (0, 0, 0))
    surface.blit(img, (20, 20 * (len(chat) + 1)))
    if (len(chat) + 1) * 20 > height:
        chat = [string]
    pygame.display.flip()

pygame.quit()
