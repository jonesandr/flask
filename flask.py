from flask import Flask, request

app = Flask(__name__)

words = {}

@app.route('/')
def home():
    return 'Welcome!'

@app.route('/add-word', methods=['GET', 'POST'])
def add_word():
    if request.method == 'POST':
        # Get the word and its meaning from the form data
        word = request.form['word']
        meaning = request.form['meaning']
        # Add the word and its meaning to the dictionary
        words[word] = meaning
        # Return a message indicating that the word was added
        return 'Word added successfully: {} - {}'.format(word, meaning)
    else:
        # Display a form for adding a new word
        return '''
            <form method="post">
                <label>Word:</label>
                <input type="text" name="word"><br>
                <label>Meaning:</label>
                <input type="text" name="meaning"><br>
                <input type="submit" value="Add Word">
            </form>
        '''
