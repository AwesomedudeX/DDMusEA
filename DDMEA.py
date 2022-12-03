import streamlit as st

sect = st.sidebar.selectbox("Navigate:", ["Homepage", "Products"])

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