import threading


def create_and_start_thread(thread_name):
	try:
		thr = threading.Thread(target=thread_name, daemon=True)
		thr.start()

		return thr

	except Exception as e:
		print(e)