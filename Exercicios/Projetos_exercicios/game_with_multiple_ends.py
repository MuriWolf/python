# 4. JOGO DE AVENTURA

# Objetivo: Crie um jogo que levará o usuário a vários possíveis finais
# de acordo com as respostas que forem passadas para ele.

import sys

import time

def restart():
    a = int(input("Digite 1 para começar denovo e 2 para parar: "))
    if a == 1:
        # começo da historia
        # momento de decisão --------------------------------------
        if len >= 0:
            print("\n* Voce acordou *\n")
            time.sleep(1.5)
            print("Jonh: Finalmente voce acordou...vamos para a taverna nova?\n")
            quest_jonh1 = int(input("Digite 1 para ir e 2 para nao ir: "))

            # alternativas para quest jonh 1:

            # digitou errado
            while quest_jonh1 != 1 and quest_jonh1 != 2:
                quest_jonh1 = int(input("\nDigite 1 para ir e 2 para nao ir: "))

            # vc seguiu o jonh / historia 1
            # momento de decisão --------------------------------------
            if quest_jonh1 == 1:
                time.sleep(1)
                print("Voce: Ok vamos.\n")
                time.sleep(0.5)
                print("chegando la..\n")
                time.sleep(0.5)
                print("Jonh: Ah, eu esqueci de falar, é meio caro as bebidas, Voce tem a grana?\n")
                quest_jonh2_1 = int(input("Digite 1 se voce tiver e 2 se nao: "))

                # digitou errado
                while quest_jonh2_1 != 1 and quest_jonh2_1 != 2:
                    quest_jonh2_1 = int(input("Digite 1 se voce tiver e 2 se nao: "))

                # voce seguiu o jonh -> voce tem o dinheiro
                if quest_jonh2_1 == 1:
                    time.sleep(1)
                    print("Voce: A sim, eu acho que tenho o suficiente.\n")
                    time.sleep(2)
                    print("Jonh: Entao vamos!\n")
                    time.sleep(2)
                    print(" * Voce e Jonh entram na taverna * \n")
                    time.sleep(2)
                    print("Jonh: Olaa Freddy! Vou querer dois hidromels!\n")
                    time.sleep(2)
                    print("Freddy: Okay, camarada.\n")
                    time.sleep(2)
                    print(" * VOCE BEBE TUDO * \n")
                    time.sleep(3)
                    print("Jonh: CArACa, tO bEm NãO.\n")
                    time.sleep(2)
                    print("Voce: nEm eU.\n")
                    time.sleep(2)
                    print("Lucas: Eae Jonh, vamos para a luta que vai ter daqui a pouco?\n")
                    time.sleep(2)
                    print("Jonh: HmMm, vAmOs pArCeIrO?\n")
                    time.sleep(2)
                    quest_jonh3_1 = int(input("Digite 1 para ir na luta e 2 para ir na sua casa: "))

                    # digitou errado
                    while quest_jonh3_1 != 1 and quest_jonh3_1 != 2:
                        quest_jonh3_1 = int(input("Digite 1 para ir na luta e 2 para ir na sua casa: "))

                    # voce seguiu o jonh -> voce tem o dinheiro -> voce vai na luta
                    if quest_jonh3_1 == 1:
                        time.sleep(1)
                        print("Voce: OkAy vAmOs: \n")
                        time.sleep(4)
                        print(" * VOCE, JONH E LUCAS CHEGAM NA LUTA * \n")
                        time.sleep(2)
                        print(" * VOCES ESTÃO NA ARQUIBANCADA, QUANDO CHEGA UM VALENTÃO * \n")
                        time.sleep(2)
                        print("Charlie, o valentão: EI VOCE!\n")
                        time.sleep(2)
                        print("VOCE: Eu?\n")
                        time.sleep(2)
                        print("Charlie, o valentão: SIM, VOCE, VAMOS BRIGAR? SEU FRANGO!\n")
                        time.sleep(2)
                        print("Voce: '-'")
                        quest_valentao = int(input("Digite 1 para lutar e 2 para não fazer nada: "))

                        # digitou errado
                        while quest_valentao != 1 and quest_valentao != 2:
                            quest_valentao = int(input("Digite 1 para lutar e 2 para não fazer nada: "))

                        # voce seguiu o jonh -> voce tem o dinheiro -> voce vai na luta -> voce vai lutar
                        if quest_valentao == 1:
                            time.sleep(1)
                            print("Voce: Ok, só vem!\n")
                            time.sleep(2)
                            print(" * BRIGA INTENSA * \n")
                            time.sleep(4)
                            print(" * VOCE PERDE FEIO * \n")
                            time.sleep(3)
                            print(" * PERDE UM DENTE TAMBEM * \n")
                            time.sleep(2)
                            print("MORAL DA HISTORIA: NAO BRIGUE BEBADO.")
                            time.sleep(2)
                            print("FIM DE JOGO")  # *****************************************
                            restart()



                        # voce seguiu o jonh -> voce tem o dinheiro -> voce vai na luta -> voce nao vai lutar
                        elif quest_valentao == 2:
                            time.sleep(1)
                            print("Voce: Nao. '-'\n")
                            time.sleep(5)
                            print("Charlie, o valentão: Então ta joia.\n")
                            time.sleep(2)
                            print("MORAL DA HISTORIA: '-'")
                            time.sleep(2)
                            print("FIM DE JOGO")  # ***********************************888
                            restart()

                    # voce seguiu o jonh -> voce tem o dinheiro -> voce nao vai na luta
                    # momento de decisão --------------------------------------
                    elif quest_jonh3_1 == 2:
                        time.sleep(1)
                        print("Voce: Ahh, eU aChO qUe é MelHOr nã...\n")
                        time.sleep(2)
                        print(" * VOMITOS INTENSOS * \n")
                        time.sleep(2)
                        print("Jonh: Ahh, CoMprEenDo, aTé MaIs.\n")
                        time.sleep(2)
                        print("Voce esta voltando para a sua casa de noite, quando aparece um grupo de bandidos.\n")
                        time.sleep(4)
                        print("Bandidos: EI, PASSA TUDO QUE VOCE TEM, AGORA!!\n")
                        quest_bandidos = int(input("Digite 1 para dar oque voce tem e 2 para nao dar: "))

                        # digitou errado
                        while quest_bandidos != 1 and quest_bandidos != 2:
                            quest_bandidos = int(input("Digite 1 para dar oque voce tem e 2 para nao dar: "))

                        # voce seguiu o jonh -> voce tem o dinheiro -> voce nao vai na luta -> voce deu oque voce tem
                        if quest_bandidos == 1:
                            time.sleep(1)
                            print("Voce: OkAy, PeGUe.\n")
                            time.sleep(2)
                            print(" * OS BANDIDOS PEGAM TUDO OQUE VOCE TEM * \n")
                            time.sleep(2)
                            print("Bandidos: Agora tu vai apanhar, hehe!\n")
                            time.sleep(2)
                            print("Voce: '-'\n")
                            time.sleep(2)
                            print(" * Voce apanha bastante * \n")
                            time.sleep(2)
                            print("MORAL DA HISTORIA: Beba com moderação.")
                            time.sleep(2)
                            print("FIM DE JOGO")  # ***********************************************
                            restart()

                        # voce seguiu o jonh -> voce tem o dinheiro -> voce nao vai na luta -> voce nao deu nada
                        elif quest_bandidos == 2:
                            time.sleep(1)
                            print("Voce: NAo VoU dAr NaDa.\n")
                            time.sleep(2)
                            print("Bandidos: ???? vai sim.\n")
                            time.sleep(2)
                            print("Voce: VEm pEgAr EnTão.\n")
                            time.sleep(2)
                            print(" * VOCE DESCE A PORRADA EM GERAL * ")
                            time.sleep(4)
                            print("Voce: CaRaCa kk, ja era, vou para a casa.\n")
                            time.sleep(2)
                            print(
                                "MORAL DA HISTORIA: SE ALGUEM TENTAR TE ROUBAR, DESCE A PORRADA NELE! (nao faça isso.)")
                            time.sleep(2)
                            print("FIM DE JOGO")  # ****************************************88
                            restart()





                # voce seguiu o jonh -> voce nao tem o dinheiro
                # momento de decisão --------------------------------------
                elif quest_jonh2_1 == 2:
                    time.sleep(1)
                    print("Voce: Nao, nao tenho nada.\n")
                    time.sleep(2)
                    print("Jonh: Oh, então adeus.\n")
                    time.sleep(2)
                    print("Voce: ??? entao ta bom\n")
                    time.sleep(2)
                    print("* Jonh saiu *\n")
                    time.sleep(3)
                    print("Voce: Nao sei oque faço ago.. espera, oque é isso?\n")
                    time.sleep(2)
                    # pergunta
                    print("Estranho escondido: ei, ei, venha aqui...\n")
                    estranho_1 = int(input("Digite 1 para seguir o estranho e 2 para nao o seguir: "))

                    # digitou errado
                    while estranho_1 != 1 and estranho_1 != 2:
                        estranho_1 = int(input("Digite 1 para seguir o estranho e 2 para nao o seguir: "))

                    # voce seguiu o jonh -> voce nao tem o dinheiro -> voce seguiu o estranho
                    if estranho_1 == 1:
                        time.sleep(1)
                        print("Voce: ok...\n")
                        time.sleep(2)
                        print("BAMM!!\n")
                        time.sleep(2)
                        print("Voce caiu em uma armadilha.\n")
                        time.sleep(2)
                        print("MORAL DA HISTORIA: Nao siga estranhos. :)\n")
                        time.sleep(2)
                        print("FIM DE JOGO")  # ***********************************************
                        restart()

                    # voce seguiu o jonh -> voce nao tem o dinheiro -> voce nao seguiu o estranho
                    # momento de decisão
                    elif estranho_1 == 2:
                        time.sleep(2)
                        print("Voce: ahh nao, adeus.\n")
                        time.sleep(2)
                        print("Estranho: Deixe disso, VENHA AQUI.\n")
                        estranho_2 = int(input("Digite 1 para CORRER e 2 para segui-lo: "))

                        # digitou errado
                        while estranho_2 != 1 and estranho_2 != 2:
                            estranho_2 = int(input("Digite 1 para CORRER e 2 para segui-lo: "))

                        # voce seguiu o jonh -> voce nao seguiu o estranho -> voce correu
                        if estranho_2 == 1:
                            time.sleep(1)
                            print("Voce em pensamento: 'Esse cara é muito estranho...\n'")
                            print(" * CORRIDA INTENSA *\n")
                            time.sleep(2)
                            print("Voce estava tao em choque que deu de cara em uma arvore...\n")
                            time.sleep(2)
                            print("Voce desmaiou e o resto ninguem sabe. :)\n")
                            time.sleep(3)
                            print("MORAL DA HISTORIA: PRESTE A ATENÇÃO QUANDO VOCE ESTIVER CORREND0.")
                            time.sleep(2)
                            print("FIM DE JOGO")  # *************************
                            restart()

                        # voce seguiu o jonh -> voce nao tem o dinheiro -> voce nao seguiu o estranho ->
                        # -> voce nao correu e seguiu o estranho
                        elif estranho_1 == 2:
                            time.sleep(1)
                            print("Voce: Ok.\n")
                            time.sleep(2)
                            print(" * Voce começa a seguir ele, então voce entra em uma floresta escura...\n")
                            time.sleep(4)
                            print("Voce perde ele de vista\n")
                            time.sleep(2)
                            print("Voce fica com medo, então voce volta e vai para bem longe...\n")
                            time.sleep(3)
                            print("Voce nunca mais ouve sobre esse estranho..\n")
                            time.sleep(2)
                            print(
                                "MORAL DA HISTORIA: nessa voce deu sorte mas NAO SIGA ESTRANHOS, serio, isso é basico!")
                            time.sleep(3)
                            print("FIM DE JOGO")
                            restart()

                            # ***********************************************



            # voce nao seguiu o jonh / historia 2
            elif quest_jonh1 == 2:
                time.sleep(1)
                print("voce: hãã, eu acho que não.\n")
                time.sleep(2)
                print("Jonh: Okay, adeus.\n")
                time.sleep(2)
                print(" * Voce volta a dormir * \n")
                time.sleep(2)
                print(" * porque voce estava com sono * \n")
                time.sleep(2)
                print("MORAL DA HISTORIA: NAO TEM MORAL DA HISTORIA.")
                print("FIM DE JOGO")
                restart()

    elif a == 2:
        print("Voce saiu do jogo.")
        sys.exit()



print("Bem vindo ao pyme!\n\nNele você tera que tomar decisões, essas deciões mudaram seu final.\nBom jogo!")

# tela inicio
inicio = str(input("\nDigite qualquer tecla para começar: "))

len = len(inicio)

# começo da historia
# momento de decisão --------------------------------------
if len >= 0:
    print("\n* Voce acordou *\n")
    time.sleep(1.5)
    print("Jonh: Finalmente voce acordou...vamos para a taverna nova?\n")
    quest_jonh1 = int(input("Digite 1 para ir e 2 para nao ir: "))

    # alternativas para quest jonh 1:

    # digitou errado
    while quest_jonh1 != 1 and quest_jonh1 != 2:
        quest_jonh1 = int(input("\nDigite 1 para ir e 2 para nao ir: "))


    # vc seguiu o jonh / historia 1
    # momento de decisão --------------------------------------
    if quest_jonh1 == 1:
        time.sleep(1)
        print("Voce: Ok vamos.\n")
        time.sleep(0.5)
        print("chegando la..\n")
        time.sleep(0.5)
        print("Jonh: Ah, eu esqueci de falar, é meio caro as bebidas, Voce tem a grana?\n")
        quest_jonh2_1 = int(input("Digite 1 se voce tiver e 2 se nao: "))

        # digitou errado
        while quest_jonh2_1 != 1 and quest_jonh2_1 != 2:
            quest_jonh2_1 = int(input("Digite 1 se voce tiver e 2 se nao: "))

        # voce seguiu o jonh -> voce tem o dinheiro
        if quest_jonh2_1 == 1:
            time.sleep(1)
            print("Voce: A sim, eu acho que tenho o suficiente.\n")
            time.sleep(2)
            print("Jonh: Entao vamos!\n")
            time.sleep(2)
            print(" * Voce e Jonh entram na taverna * \n")
            time.sleep(2)
            print("Jonh: Olaa Freddy! Vou querer dois hidromels!\n")
            time.sleep(2)
            print("Freddy: Okay, camarada.\n")
            time.sleep(2)
            print(" * VOCE BEBE TUDO * \n")
            time.sleep(3)
            print("Jonh: CArACa, tO bEm NãO.\n")
            time.sleep(2)
            print("Voce: nEm eU.\n")
            time.sleep(2)
            print("Lucas: Eae Jonh, vamos para a luta que vai ter daqui a pouco?\n")
            time.sleep(2)
            print("Jonh: HmMm, vAmOs pArCeIrO?\n")
            time.sleep(2)
            quest_jonh3_1 = int(input("Digite 1 para ir na luta e 2 para ir na sua casa: "))

            # digitou errado
            while quest_jonh3_1 != 1 and quest_jonh3_1 != 2:
                quest_jonh3_1 = int(input("Digite 1 para ir na luta e 2 para ir na sua casa: "))


            # voce seguiu o jonh -> voce tem o dinheiro -> voce vai na luta
            if quest_jonh3_1 == 1:
                time.sleep(1)
                print("Voce: OkAy vAmOs: \n")
                time.sleep(4)
                print(" * VOCE, JONH E LUCAS CHEGAM NA LUTA * \n")
                time.sleep(2)
                print(" * VOCES ESTÃO NA ARQUIBANCADA, QUANDO CHEGA UM VALENTÃO * \n")
                time.sleep(2)
                print("Charlie, o valentão: EI VOCE!\n")
                time.sleep(2)
                print("VOCE: Eu?\n")
                time.sleep(2)
                print("Charlie, o valentão: SIM, VOCE, VAMOS BRIGAR? SEU FRANGO!\n")
                time.sleep(2)
                print("Voce: '-'")
                quest_valentao = int(input("Digite 1 para lutar e 2 para não fazer nada: "))

                # digitou errado
                while quest_valentao != 1 and quest_valentao != 2:
                    quest_valentao = int(input("Digite 1 para lutar e 2 para não fazer nada: "))

                # voce seguiu o jonh -> voce tem o dinheiro -> voce vai na luta -> voce vai lutar
                if quest_valentao == 1:
                    time.sleep(1)
                    print("Voce: Ok, só vem!\n")
                    time.sleep(2)
                    print(" * BRIGA INTENSA * \n")
                    time.sleep(4)
                    print(" * VOCE PERDE FEIO * \n")
                    time.sleep(3)
                    print(" * PERDE UM DENTE TAMBEM * \n")
                    time.sleep(2)
                    print("MORAL DA HISTORIA: NAO BRIGUE BEBADO.")
                    time.sleep(2)
                    print("FIM DE JOGO") # *****************************************
                    restart()



                # voce seguiu o jonh -> voce tem o dinheiro -> voce vai na luta -> voce nao vai lutar
                elif quest_valentao == 2:
                    time.sleep(1)
                    print("Voce: Nao. '-'\n")
                    time.sleep(5)
                    print("Charlie, o valentão: Então ta joia.\n")
                    time.sleep(2)
                    print("MORAL DA HISTORIA: '-'")
                    time.sleep(2)
                    print("FIM DE JOGO") # ***********************************888
                    restart()

            # voce seguiu o jonh -> voce tem o dinheiro -> voce nao vai na luta
            # momento de decisão --------------------------------------
            elif quest_jonh3_1 == 2:
                time.sleep(1)
                print("Voce: Ahh, eU aChO qUe é MelHOr nã...\n")
                time.sleep(2)
                print(" * VOMITOS INTENSOS * \n")
                time.sleep(2)
                print("Jonh: Ahh, CoMprEenDo, aTé MaIs.\n")
                time.sleep(2)
                print("Voce esta voltando para a sua casa de noite, quando aparece um grupo de bandidos.\n")
                time.sleep(4)
                print("Bandidos: EI, PASSA TUDO QUE VOCE TEM, AGORA!!\n")
                quest_bandidos = int(input("Digite 1 para dar oque voce tem e 2 para nao dar: "))

                # digitou errado
                while quest_bandidos != 1 and quest_bandidos != 2:
                    quest_bandidos = int(input("Digite 1 para dar oque voce tem e 2 para nao dar: "))

                # voce seguiu o jonh -> voce tem o dinheiro -> voce nao vai na luta -> voce deu oque voce tem
                if quest_bandidos == 1:
                    time.sleep(1)
                    print("Voce: OkAy, PeGUe.\n")
                    time.sleep(2)
                    print(" * OS BANDIDOS PEGAM TUDO OQUE VOCE TEM * \n")
                    time.sleep(2)
                    print("Bandidos: Agora tu vai apanhar, hehe!\n")
                    time.sleep(2)
                    print("Voce: '-'\n")
                    time.sleep(2)
                    print(" * Voce apanha bastante * \n")
                    time.sleep(2)
                    print("MORAL DA HISTORIA: Beba com moderação.")
                    time.sleep(2)
                    print("FIM DE JOGO") # ***********************************************
                    restart()

                # voce seguiu o jonh -> voce tem o dinheiro -> voce nao vai na luta -> voce nao deu nada
                elif quest_bandidos == 2:
                    time.sleep(1)
                    print("Voce: NAo VoU dAr NaDa.\n")
                    time.sleep(2)
                    print("Bandidos: ???? vai sim.\n")
                    time.sleep(2)
                    print("Voce: VEm pEgAr EnTão.\n")
                    time.sleep(2)
                    print(" * VOCE DESCE A PORRADA EM GERAL * ")
                    time.sleep(4)
                    print("Voce: CaRaCa kk, ja era, vou para a casa.\n")
                    time.sleep(2)
                    print("MORAL DA HISTORIA: SE ALGUEM TENTAR TE ROUBAR, DESCE A PORRADA NELE! (nao faça isso.)")
                    time.sleep(2)
                    print("FIM DE JOGO") # ****************************************88
                    restart()





        # voce seguiu o jonh -> voce nao tem o dinheiro
        # momento de decisão --------------------------------------
        elif quest_jonh2_1 == 2:
            time.sleep(1)
            print("Voce: Nao, nao tenho nada.\n")
            time.sleep(2)
            print("Jonh: Oh, então adeus.\n")
            time.sleep(2)
            print("Voce: ??? entao ta bom\n")
            time.sleep(2)
            print("* Jonh saiu *\n")
            time.sleep(3)
            print("Voce: Nao sei oque faço ago.. espera, oque é isso?\n")
            time.sleep(2)
            # pergunta
            print("Estranho escondido: ei, ei, venha aqui...\n")
            estranho_1 = int(input("Digite 1 para seguir o estranho e 2 para nao o seguir: "))

            # digitou errado
            while estranho_1 != 1 and estranho_1 != 2:
                estranho_1 = int(input("Digite 1 para seguir o estranho e 2 para nao o seguir: "))

            # voce seguiu o jonh -> voce nao tem o dinheiro -> voce seguiu o estranho
            if estranho_1 == 1:
                time.sleep(1)
                print("Voce: ok...\n")
                time.sleep(2)
                print("BAMM!!\n")
                time.sleep(2)
                print("Voce caiu em uma armadilha.\n")
                time.sleep(2)
                print("MORAL DA HISTORIA: Nao siga estranhos. :)\n")
                time.sleep(2)
                print("FIM DE JOGO") # ***********************************************
                restart()

            # voce seguiu o jonh -> voce nao tem o dinheiro -> voce nao seguiu o estranho
            # momento de decisão
            elif estranho_1 == 2:
                time.sleep(2)
                print("Voce: ahh nao, adeus.\n")
                time.sleep(2)
                print("Estranho: Deixe disso, VENHA AQUI.\n")
                estranho_2 = int(input("Digite 1 para CORRER e 2 para segui-lo: "))

                # digitou errado
                while estranho_2 != 1 and estranho_2 != 2:
                    estranho_2 = int(input("Digite 1 para CORRER e 2 para segui-lo: "))

                # voce seguiu o jonh -> voce nao seguiu o estranho -> voce correu
                if estranho_2 == 1:
                    time.sleep(1)
                    print("Voce em pensamento: 'Esse cara é muito estranho...\n'")
                    print(" * CORRIDA INTENSA *\n")
                    time.sleep(2)
                    print("Voce estava tao em choque que deu de cara em uma arvore...\n")
                    time.sleep(2)
                    print("Voce desmaiou e o resto ninguem sabe. :)\n")
                    time.sleep(3)
                    print("MORAL DA HISTORIA: PRESTE A ATENÇÃO QUANDO VOCE ESTIVER CORREND0.")
                    time.sleep(2)
                    print("FIM DE JOGO") # *************************
                    restart()

                # voce seguiu o jonh -> voce nao tem o dinheiro -> voce nao seguiu o estranho ->
                # -> voce nao correu e seguiu o estranho
                elif estranho_1 == 2:
                    time.sleep(1)
                    print("Voce: Ok.\n")
                    time.sleep(2)
                    print(" * Voce começa a seguir ele, então voce entra em uma floresta escura...\n")
                    time.sleep(4)
                    print("Voce perde ele de vista\n")
                    time.sleep(2)
                    print("Voce fica com medo, então voce volta e vai para bem longe...\n")
                    time.sleep(3)
                    print("Voce nunca mais ouve sobre esse estranho..\n")
                    time.sleep(2)
                    print("MORAL DA HISTORIA: nessa voce deu sorte mas NAO SIGA ESTRANHOS, serio, isso é basico!")
                    time.sleep(3)
                    print("FIM DE JOGO")
                    restart()

                    # ***********************************************



    # voce nao seguiu o jonh / historia 2
    elif quest_jonh1 == 2:
        time.sleep(1)
        print("voce: hãã, eu acho que não.\n")
        time.sleep(2)
        print("Jonh: Okay, adeus.\n")
        time.sleep(2)
        print(" * Voce volta a dormir * \n")
        time.sleep(2)
        print(" * porque voce estava com sono * \n")
        time.sleep(2)
        print("MORAL DA HISTORIA: NAO TEM MORAL DA HISTORIA.")
        print("FIM DE JOGO")
        restart()


