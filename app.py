from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name' : 'python'}, {'name' : 'Go'}, {'name' : 'JavaScript'}]

# Get methods
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It has worked!!!'})

@app.route('/lang', methods=['GET'])
def return_all():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
    langs =[language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

# POST Method
@app.route('/lang', methods=['POST'])
def add_one():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})

# PUT Method
@app.route('/lang/<string:name>', methods=['PUT'])
def edit_one(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})

#Delete Method
@app.route('/lang/<string:name>', methods=['DELETE'])
def remove_one(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages })

if __name__ == '__main__':
    app.run(debug=True)
