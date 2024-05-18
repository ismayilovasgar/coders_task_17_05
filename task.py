# Folder taskı

# 1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
# 2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  adında alt
# kateqoriya(subdirectory) yaradırıq.
# 3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik.
# (şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  daha
#  sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
# 4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları subdirectorydən
# çıxarıb Example directory-sinə göndərirsiniz.

import os, pathlib, shutil, fnmatch

main_path = os.path.dirname(__file__)
os.makedirs(main_path + "/Example/Subdirectory")

with open(main_path + "/text_file.txt", encoding="utf-8", mode="+x") as text_file:
    text_file.write("text file ")

with pathlib.Path(main_path) as my_file:
    for i in my_file.iterdir():
        if i.name.endswith(".txt") or i.name.endswith(".jpg"):
            shutil.move(i, main_path + "/Example/subdirectory")

# diger yolu
# shutil.move(main_path + "/text_file.txt", main_path + "/Example/subdirectory/")
# shutil.move(main_path + "/miller.jpg", main_path + "/Example/subdirectory/")


for i in pathlib.Path(main_path + "/Example/subdirectory").iterdir():
    if i.is_file() and fnmatch.fnmatch(i, "*.txt"):
        shutil.move(i, main_path+"/Example")
