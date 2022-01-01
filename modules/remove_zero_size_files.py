# Required modules
import pandas as pd
import os
def remove_zero_size_file(show_process=False, save_to_csv=False):
    '''
        Removes Zero Size file from the label data and merges with the given sentence
        
        showProcess:
            prints the process if yes. Default false.
            The files that we have taken has atleast 80 different files with zero file size which cannot be processes and as for the labels, those zero file's labels should be removed and in that label sentenceId is given which would need an actual sentence to proceed furthur with the processing. Hence, The following function named `remove_zero_size_file()` is created which does all of the above tasks and returns the required label and saves it as an csv file for future use.
            
    '''
    path = os.path.abspath(os.getcwd())
    if show_process:
        print("Current File Path is:- {}".format(path))
    file_path = os.path.join(path, 'audioFiles')
    if show_process:
        print("Path of the audioFiles is found!")
    file_list = [x for x in os.listdir(file_path) if x.split('.')[-1]=='wav']
    if show_process:
        print("The list of the audio files found!")
    # Getting file size
    file_size = [os.stat(os.path.join(file_path, x)).st_size for x in file_list]
    if show_process:
        print("The list of the audio file size found!")
        print("Note:- Each index in file size represents same index in audio files list.")
    # getting label json_file
    json_file = os.path.join(path, 'labels/data.json')
    sentence_file = os.path.join(path, 'labels/sentenceLabels.json')
    if show_process:
        print("Path of data.json:- {}".format(json_file))
        print("Path of data.json:- {}".format(sentence_file))
    # Reading dataFrame as json
    df1 = pd.read_json(json_file)
    df2 = pd.read_json(sentence_file)
    if show_process:
        print("Json file loaded!")
    # File without zero size files
    file_removing_zero = [filename for index, filename in enumerate(file_list) if file_size[index]!=0]
    if show_process:
        print("List of file with no zero bytes files found!")
    # File of zero size files
    file_to_be_removed = [filename for index, filename in enumerate(file_list) if file_size[index]==0]
    if show_process:
        print("List of file with only zero byte files found!")
    # list of indexs to be removed
    list_of_index_to_be_removed = []
    for index, filename in enumerate(file_to_be_removed):
        file = filename.split('.')[0]
        list_of_index_to_be_removed.append(df1.index[df1['fileName'] == file].tolist())
    list_of_index_to_be_removed = [x[0] for x in list_of_index_to_be_removed]
    if show_process:
        print("The list of indexs in the files list to be removed found!")
    # Removing zero bytes files from the index
    df1.drop(list_of_index_to_be_removed, axis = 0, inplace=True)
    if show_process:
        print("The zero bytes files are now removed from the dataframe.")
    # Combinding two dataframes
    df2.rename(columns={"_id": "sentenceId"}, inplace=True)
    df = pd.merge(df1, df2, on='sentenceId')
    df.drop('sentenceId', axis=1, inplace=True)
    if show_process:
        print("New Dataframe creation completed!")
    # Exporting the file
    if save_to_csv:
        df.to_csv(os.path.join(path,'labels/filtered.csv'), index=False)
        if show_process:
            print("File is now exported to a csv file.")
    return df