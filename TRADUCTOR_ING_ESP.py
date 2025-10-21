"""
TRADUCTOR_ING_ESP
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googletrans import Translator
import textwrap

def read_and_chunk_file(file_path, chunk_size=4500):
    # Leer el documento completo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Dividir el documento en chunks
    chunks = textwrap.wrap(content, chunk_size, break_long_words=False, replace_whitespace=False)
    return chunks

def translate_chunks(chunks, src_lang='en', dest_lang='es'):
    translator = Translator()
    translated_chunks = []

    for i in range(len(chunks)):
        # Traducir cada chunk
        translated_chunk = translator.translate(chunks[i], src=src_lang, dest=dest_lang).text
        translated_chunks.append(translated_chunk)

    return translated_chunks

def save_translated_chunks(translated_chunks, output_file_path):
    # Juntar las partes traducidas
    full_translation = ' '.join(translated_chunks)

    # Guardar en un nuevo archivo
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(full_translation)

# Uso
input_file_path = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\SEMANA 8\\StrategyzerWebinarValuePropositionCanvasBestPractices.txt"
output_file_path = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\GER-TI CATO1-2024\\Cursos\\SEMANA 8\\Texto_video_2.txt"

chunks = read_and_chunk_file(input_file_path)
translated_chunks = translate_chunks(chunks)
save_translated_chunks(translated_chunks, output_file_path)


# In[ ]:






if __name__ == "__main__":
    pass
