from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3
import hashlib
import datetime

def update(ip_address, session_id, user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET ip_address = ?, cookie = ? WHERE id = ?', [ip_address, session_id, user[0]])
    conn.commit()
    conn.close()