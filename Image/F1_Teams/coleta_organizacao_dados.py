# %%
#Codigo js a ser executado no terminal/console do browser... na tela de resultados do google imagens
'''urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('src')?el.getAttribute('src'):el.getAttribute('data-iurl')); 
window.open('data:text/csv;charset=utf-8,'+ escape(urls.join('\n')));'''

# %%
import pandas as pd

# %%
''''williams','ferrari', 'alpine','alphatauri','redbull',
'astonmartin','haas','alpharomeo','mercedes','mclaren']
'''


# %%
import requests
import os
equipes = ['williams','ferrari', 'alpine','alphatauri','redbull','astonmartin','haas','alpharomeo','mercedes','mclaren']
def mantem_links(x): 
    if 'https' in x:
        return x
    else:
        return False

for equipe in equipes:
    df = pd.read_csv('./CSVs/{}.csv'.format(equipe),header=None)
    df.columns = ['LINK','0']
    df.LINK = df.LINK.apply(mantem_links)
    df = df[df.LINK != False]
    dir = './{}'.format(equipe)
    try:
        os.mkdir(dir)
    except:
        pass
    print('Preparando os arquivos da equipe {} ...'.format(equipe))
    for indice,linha in enumerate (df.LINK):
        response = requests.get(linha)
        file = open("./{}/{}.png".format(equipe,equipe + '_' + str(indice)),'wb')
        file.write(response.content)
        file.close()

# %%



