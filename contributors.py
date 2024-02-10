import streamlit as st
from config import CONTRIBUTORS

def contributors_page():
    st.balloons()
    
    with open("assets/misc/contributors.txt", "r") as f:
        data = f.read().splitlines()
        full_string = ""
        
        for i in range(0, len(data), 3):
            try:
                contributor1 = data[i].split(",")[0].strip().title()
                contributor2 = data[i + 1].split(",")[0].strip().title()
                contributor3 = data[i + 2].split(",")[0].strip().title()

                contributors = f"""<tr>
                    <td>{contributor1}</td>
                    <td>{contributor2}</td>
                    <td>{contributor3}</td>
                </tr>
                """
                full_string += contributors
            
            except IndexError:
                if len(data[i:])==2:
                    full_string += f"""<tr>
                            <td>
                                {data[i:][0].split(",")[0].strip().title()}
                            </td>
                            <td>
                                {data[i:][1].split(",")[0].strip().title()}
                            </td>
                        </tr>
                    """
                elif len(data[i:])==1:
                    full_string += f"""<tr>
                            <td>
                                {data[i:][0].split(",")[0].strip().title()}
                            </td>
                        </tr>
                    """

        st.write(CONTRIBUTORS.format(full_string), unsafe_allow_html=True)
        
if __name__ == "__main__":
    contributors_page()