from flask import jsonify
from flask import request
import json
from flask import Flask

app=Flask(__name__)

def get_word(word):
    return word**2     #{}

@app.route('/nlp/words',methods=['GET','POST'])
def nlp_service():
    data=request.get_data()
    result_data=json.loads(data)
    word=result_data.get('word','')
    value=get_word(word)
    return jsonify({'code':200,'result':value})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=50001)

# from flask import jsonify
# from flask import request
# import json
# from flask import Flask
# from word2vec import f
# app=Flask(__name__)
#
# # def get_word(word):#定义一个函数，接受一个单词作为参数，目前函数体仅返回接收到的单词。
# #     return word
#
# @app.route("/nlp/words",methods=["GET","POST"])
# def nlp_service():
#     data=request.get_data()
#     result_data=json.loads(data)#{}
#     word1 = result_data.get("word1","")
#     word2 = result_data.get("word2", "")
#     value = f(word1,word2)
#     return jsonify({"code":200,"result":value})
# if __name__ == "__main__":
#     app.run(host='0.0.0.0',port=50001)


