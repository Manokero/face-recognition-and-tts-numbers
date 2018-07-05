import pyaudio
import wave
import sys

CHUNK = 1024

dir_number = './voice_number/'

special_numbers = ['1','2', '3', '4', '5']
special_speech_numbers = [10, 20, 100]

def speech_number(numbers=[]):
    num = 0
    for state in range(len(numbers), 0, -1):

        n = int("".join(numbers[-state:]))

        if n in special_speech_numbers:
            wf = wave.open(f'{dir_number}specials/{n}.wav', 'rb')
            speech(wf)
            # print('special n>', n)
            break

        if state == 2 and numbers[num] == '1' and numbers[num+1] in special_numbers:
            descens(numbers[num+1])
            break

        if numbers[num] == '0':
            num = num + 1
            continue

        if state == 4:
            wf = wave.open(f'{dir_number}1/{numbers[num]}.wav', 'rb')
            wf_mil = wave.open(f'{dir_number}mil.wav', 'rb')

            if not numbers[num] == '1':
                speech(wf)

            speech(wf_mil)

            num = num + 1
            continue

        wf = wave.open(f'{dir_number}{state}/{numbers[num]}.wav', 'rb')
        num = num + 1

        speech(wf)

def descens(number, state='specials'):
    wf = wave.open(f'{dir_number}{state}/{number}.wav', 'rb')

    speech(wf)

def speech(wf=''):
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

