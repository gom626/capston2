# Create your views here.
from django.shortcuts import render
#import importlib
from confluent_kafka import Producer
import json
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from confluent_kafka import *
from django.http import HttpResponse, HttpResponseRedirect

settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}
'''
cs = Consumer(settings)
tp = TopicPartition('mytopic2', 0, 0)
low, high = cs.get_watermark_offsets(tp)
cs.assign([tp])

print(high)
test = {'cont' : []}

i=0
while i<high:
    msg = cs.poll(0.1)
    if msg is None:
        continue
    elif not msg.error():
        i = i+1
        test['cont'].append(format(msg.value())[2:-1])
        
    elif msg.error().code() == KafkaError._PARTITION_EOF:
        print('End of partition reached {0}/{1}' .format(msg.topic(), msg.partition()))
    else:
        print('Error occured: {0}'.format(msg.error().str()))
print(test)
'''
#BoardId = 1
def index(request,board_id):
    #BoardId = board_id
    #p = Producer({'bootstrap.servers': 'localhost:9092'})
    #p.produce(board_id, value='test')
    #p.produce(BoardId, value=request.POST['content'])
    
    #print(request.POST['content'])
    #p.flush(30)


    cs = Consumer(settings)
    #tp = TopicPartition('mytopic2', 0, 0)
    tp = TopicPartition(board_id, 0, 0)

    low, high = cs.get_watermark_offsets(tp)
    cs.assign([tp])

    print(high)
    test = {'cont' : [], 'BoardId' : []}
    test['BoardId'].append(board_id)
    i=0
    
    while i<high:
        msg = cs.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            #print('Received message: {0}'.format(msg.value()))
            i = i+1
            #test['cont'].append(format(msg.value())[2:-1])
            test['cont'].append(msg.value().decode('utf-8'))
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}' .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))
    print(test)
    
    return render(request, 'chat/index.html', test)
    #return render(request, 'chat/index.html', context)
    #return render(request, 'chat/index.html')

def submit(request, board_id):
    if request.method == "POST":
        p = Producer({'bootstrap.servers': 'localhost:9092'})
        #p.produce('mytopic2', value=request.POST['content'])
        p.produce(board_id, value=request.POST['content'])
        #print(board_id)
        print(request.POST['content'])
        p.flush(30)    
    return HttpResponseRedirect('/chat/index/' + board_id)
    #return render(request,"chat/index.html")
