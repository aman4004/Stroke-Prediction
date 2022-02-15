import joblib
import numpy as np
import pandas as pd
import warnings

# hiding warnings
warnings.filterwarnings('ignore')

# model
model = joblib.load('SVC_model.p')

# Input format:
inpfmt = ['age', 'hypertension', 'bmi',
          'work_type_Self-employed', 'work_type_children']


# model to make prediction
def predictor(data, show_output=True):
    data_ = np.array(data).reshape(1, -1)

    result = model.predict(data_)
    if show_output:
        print(f'\nYour Input: {dict(zip(inpfmt, data))}')
        if result == [1]:
            print(f'Prediction: {result}-Stroke Patient\n')
        else:
            print(f'Prediction: {result}-Non-Stroke Patient\n')
    else:
        return int(result)


# user input
while True:
    print('='*10, "Stroke Predictor is ready to run", '='*10)

    # break or continue
    quit_or_run = input("Enter (c) to continue or (q) to quit: ")
    if quit_or_run.lower() == 'q':
        break

    # file type
    inp_typ = input('Enter (f) for csv_file input or (s) for single_input: ')

    if inp_typ.lower() == 's':
        # user input
        try:
            inp = eval(
                input(f"Enter a list in following format\n{str(inpfmt)}\nYour input: "))
            # prediction
            predictor(inp)
        except Exception as e:
            print(e)

    elif inp_typ.lower() == 'f':
        # handling file
        try:
            file_name = input('Enter your file location: ')
            test = pd.read_csv(file_name)

            # prediction
            output = []
            output_file = open('output.csv', 'w')

            for i in test.values:
                result = predictor(i, show_output=False)
                output.append(result)
                output_file.write(f"{str(result)}\n")

            output_file.close()

            print(output)
            print('\nYour output is also saved in a "output.csv" file :)')

        except Exception as e:
            print(e)
