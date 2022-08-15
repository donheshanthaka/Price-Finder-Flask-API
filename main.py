from app import create_app

app = create_app()

if __name__ == '__main__':
    # When using the android emulator
    # app.run(host="0.0.0.0", port=8000)
    app.run() # For production
