# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# In[4]:

# new import
import sys
import os
import json
from flask import Flask

# new import
from flask import jsonify

# new code from https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/natural_language_understanding_v1.py
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as \
       features

app = Flask("NLU Application")

# new code from https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/natural_language_understanding_v1.py	    
nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
       version='2017-02-27',
       username=os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_USERNAME'),
       password=os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_PASSWORD'))

# New code for testing NLU features:
@app.route("/")
def default_welcome():
        return 'Welcome to the NLU Application!'

@app.route("/entities")
def eval_entities():
        response = nlu.analyze(
                text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
                'Superman fears not Banner, but Wayne.',
                features=[features.Entities()])
        return jsonify(response)

@app.route("/keywords")
def eval_keywords():
        response = nlu.analyze(
                text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
                'Superman fears not Banner, but Wayne.',
                features=[features.Keywords()])
        return jsonify(response)

@app.route("/categories")
def eval_categories():
        response = nlu.analyze(
                url='www.cnn.com',
                features=[features.Categories()])
        return jsonify(response) 

@app.route("/concepts")
def eval_concepts():
        response = nlu.analyze(
                text='Natural Language Understanding uses natural language processing to analyze text.',
                features=[features.Concepts()])
        return jsonify(response)

@app.route("/emotion")
def eval_emotion():
        response = nlu.analyze(
                text='I love apples, but I hate oranges.',
                features=[features.Emotion(targets=['apples','oranges'])])
        return jsonify(response) 

@app.route("/metadata")
def eval_metadata():
        response = nlu.analyze(
                url='https://www.ibm.com/blogs/think/2017/01/cognitive-grid/',
                features=[features.MetaData()])
        return jsonify(response)

@app.route("/relations")
def eval_relations():
        response = nlu.analyze(
                text='The Nobel Prize in Physics 1921 was awarded to Albert Einstein.',
                features=[features.Relations()])
        return jsonify(response)

@app.route("/semantic_roles")
def eval_semantic_roles():
        response = nlu.analyze(
                text='In 2011, Watson competed on Jeopardy!',
                features=[features.SemanticRoles()])
        return jsonify(response)

@app.route("/sentiment")
def eval_Sentiment():
        response = nlu.analyze(
                text='Thank you and have a nice day!',
                features=[features.Sentiment()])
        return jsonify(response)

#port = os.getenv('PORT', '5000')
if __name__ == "__main__":
       app.run(host='0.0.0.0',debug=True,port=int(os.getenv('PORT',8080)))
