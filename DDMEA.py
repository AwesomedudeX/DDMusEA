import streamlit as st

sect = st.sidebar.selectbox("Navigate:", ["Homepage", "Products", "About"])

if sect == "Homepage":
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Disco Dave\'s MusEA</h1>', unsafe_allow_html=True)
	st.write("Disco Dave’s MusEA is a service that provides YOU the best possible DJ service at parties, social gatherings, ceremonies, and clubs, all for a great price!")
	st.header("-"*61)
	st.write("Our party services include: smoke machines, multiple options of lighting such as par lights or strip lights, disco balls and rentable limosines for the party. We bring 4 LyxPro SPA-10 10\" Portable Professional PA Speakers with us for the best sound quality. Disco Dave also is well-versed in DiscoCity Pro’s many advanced features, and he uses that with the ElectroWorld X Series 9 DJ board to make every night one you won’t forget.")

elif sect == "Products":

	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Products:</h1>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Karaoke Microphones: $20</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Disco Balls: $30</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Spotlights: $160</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Cost for One Hour For Parties: $120</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Cost For One Hour for Weddings: $150</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Dance Floor: $30</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">+1 Speaker: $60</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Limousine rentals: $1500</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">DiscoCity Software: DDMEA Promo Code</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Dave’s DJ SoundBoard: ElectroWorld X Series 9: $1000</h4>', unsafe_allow_html=True)

elif sect == "About":

	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">About Dave:</h1>', unsafe_allow_html=True)
	st.markdown(f'<h5 style="color:#00FF55;font-size:17px;">Dave started out playing in a rock band in college and spent 3 years as a sound engineer before changing careers. He’s been a DJ for 4 years and creates all of his own music using only the newest modern software. You might’ve even seen Dave in places like the Fortnite World Cup and Jay-Z’s wedding.  He’d just hit the turning point in his career 4 months ago when Dave surpassed all DJ services as the main DJ for huge celebrations. Dave’s also an on-time, cash upfront kind of guy, so he likes to be physically present at the right times to blast some beats that everyone’s probably gonna be vibin’ to for the next month at least. He really enjoys his current career and spends most of his time jamming out to the latest hits or just vibing to some nice beats. When he isn’t, he’s usually sleeping in his room with his dog, Bruno, or enjoying some game time while listening to his latest mixes.</h5>', unsafe_allow_html=True)
