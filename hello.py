from flask import Flask

# Membuat objek Flask
app = Flask(__name__,
    static_url_path='',  # Perbaiki 'static_irl_path' menjadi 'static_url_path'
    static_folder='web/static',
    template_folder='web/templates')

# Menentukan route ke halaman utama
@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route('/foobar')
def foobar():
    return 'Hi there, foobar!'

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)