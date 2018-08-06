def save_message(cursor, message_id, message_text):
	cursor.execute("""INSERT INTO MESSAGES VALUES (?,?)""", (message_id, message_text))


def get_message(cursor, message_id):
	cursor.execute("""SELECT * FROM MESSAGES WHERE ID = ?""", (message_id,))
	return cursor.fetchone()


def delete_message(cursor, message_id):
	cursor.execute("""DELETE * FROM MESSAGES WHERE ID = ?""", (message_id))


def add_user(cursor, user):
	cursor.execute("""INSERT INTO USERS VALUES (?,?,?,?,?)""", (user.id, user.first_name, user.last_name, user.username, 0))


def reg_user(cursor, user_id):
	cursor.execute("""UPDATE USERS SET REGISTERED = 1 WHERE ID = ?""", (user_id,))


def get_user(cursor, user_id):
	cursor.execute("""SELECT * FROM USERS WHERE ID = ?""", (user_id,))
	return cursor.fetchone()
