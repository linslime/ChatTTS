import torch
import ChatTTS
from IPython.display import Audio

chat = ChatTTS.Chat()
chat.load_models(source='local', local_path='./data')

texts = ["So we found being competitive and collaborative was a huge way of staying motivated towards our goals",]*3 \
        + ["我觉得像我们这些写程序的人，他，我觉得多多少少可能会对开源有一种情怀在吧我觉得开源是一个很好的形式。"]*3
wavs = chat.infer(texts, use_decoder=True)