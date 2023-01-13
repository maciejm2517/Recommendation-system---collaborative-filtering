import gui
import recomender
import pandas as pd
from tkinter import messagebox

msg_box_anime = messagebox.askquestion('Choose dataset', 'Do you want to use anime reviews dataset? (imported from .pickle file)',
                                        icon='warning')

if msg_box_anime == 'yes':
    recomender.item_similarity_df=pd.read_pickle('item_similarity_df.pickle')
    names=recomender.get_names()
    app=gui.Gui(names)

msg_box_movies = messagebox.askquestion('Choose dataset', 'Do you want to use movies reviews dataset?',
                                        icon='warning')
if msg_box_movies =='yes':
    recomender.item_similarity_df=recomender.recommender_module()
    names=recomender.get_names()
    app=gui.Gui(names)