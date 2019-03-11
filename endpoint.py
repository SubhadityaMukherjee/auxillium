from flask import Flask
import problem as pb
app = Flask(__name__)
l= pb.connect_iss_to_ngo()

@app.route('/')
def hello_world():
   return str(l)

if __name__ == '__main__':
   app.run()