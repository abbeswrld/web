import threading


def create_and_start_thread(thread_name):
	threading.Thread(target=thread_name, daemon=True).start()