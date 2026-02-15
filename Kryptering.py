#importer pakker
import streamlit as st

#alfabet string
abc = "abcdefghijklmnopqrstuvwxyzæøå,.-!@#£$%&/{([)]}?+*'|`><_1234567890=:;^äëüïöâêûÿîôñ "
#enkrypterings funktion
def ekrpt(msg,key):
    encrypt = ""
    for index, char in enumerate(msg.lower()):
        #går igennem beskeden en karakter ad gangen og får dens index nr.
        if char not in abc:
            encrypt+= char
            #beholder de tegn der ikke er med i vores str.
            continue
        #giver tal for hver bogstav
        msg_pos = abc.index(char)
        #nøglens tal med modulus til længden af nøglen i tilfælde af at nøglen er kortere end beskeden
        key_pos = abc.index(key[index % len(key)].lower())
        #summen af nøglen og ordets placering og sørger for den ikke er for lang ved at bruge modulo
        new_pos = (msg_pos+key_pos) % len(abc)
        #finder det tilsvarende tegn
        encrypt += abc[new_pos]
    return encrypt
#dekrypterings funktion, den er funktionelt den samme som enkrypteringen, den trækker bare fra.
def dkrpt(msg,key):
    decrypt = ""
    for index, char in enumerate(msg.lower()):
        if char not in abc:
            decrypt+= char
            continue
        msg_pos = abc.index(char)
        key_pos = abc.index(key[index % len(key)].lower())
        #her trækker vi tegnet position fra nøglens, så vi får den originale besked.
        new_pos = (msg_pos-key_pos) % len(abc)
        decrypt += abc[new_pos]
    return decrypt
        
st.title("D&J Kryptering")

key = st.text_input("Indskriv din nøgle")
msg = st.text_input("Indskriv din besked")

if st.button("Dekryptering"):
    if len(msg)>0 and len(key)>0:
        result = dkrpt(msg,key)
        st.success(f"{result}")
    else:
        st.warning("Indtast både nøgle og besked")

if st.button("Enkryptering"):
    #fejl kode hvis ikke felterne er udfyldt korrekt.
    if len(msg)>0 and len(key)>0:
        result = ekrpt(msg,key)
        st.success(f"{result}")
    else:
        st.warning("Indtast både nøgle og besked")

