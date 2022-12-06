import streamlit as st
from datetime import datetime as dt

sect = st.sidebar.selectbox("Navigate:", ["Homepage", "Products", "Booking", "About"])

if sect == "Homepage":
	st.write("Note: This website is not a real website, and was made for a school project. Don't worry about any information being stolen, as none will be saved.")
	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Disco Dave\'s MusEA</h1>', unsafe_allow_html=True)
	st.markdown(f'<h2 style="color:#0066FF;font-size:25px;">"Your one-way ticket to the virtual music world!"</h2>', unsafe_allow_html=True)
	st.write("Disco Dave’s MusEA is a service that provides YOU the best possible DJ service at parties, social gatherings, ceremonies, and clubs, all for a great price!")
	st.write("Our party services include: smoke machines, multiple options of lighting such as par lights or strip lights, disco balls and rentable limosines for the party. We bring 4 LyxPro SPA-10 10\" Portable Professional PA Speakers with us for the best sound quality. Disco Dave also is well-versed in DiscoCity Pro’s many advanced features, and he uses that with the ElectroWorld X Series 9 DJ board to make every night one you won’t forget.")
	st.markdown(f'<h2 style="color:#0066FF;font-size:25px;">A Word From Our Sponsor and Partner</h2>', unsafe_allow_html=True)
	st.write("\"Lit buisiness, wish more services like these existed 🔥\" - Noisestorm (Partner)")
	st.write("\"Glad to partner up! Was a great investment on our end\" - Gameloft (Sponsor)")
	st.header("")
	st.image("Logo.PNG")

elif sect == "Products":

	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">Products:</h1>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Karaoke Microphones: $20</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Disco Balls: $30</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Spotlights: $160</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Cost for One Hour For Parties: $120</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Cost For One Hour for Weddings: $150</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">+1 Speaker: $60</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Limousine rentals: $1500</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Dave’s DJ SoundBoard: ElectroWorld X Series 9: $1000</h4>', unsafe_allow_html=True)
	st.markdown(f'<h4 style="color:\'white\';font-size:18px;">DiscoCity Software: Use Promo Code \'DDMEA\' for a free trial month and a 50% discount on monthly payments for a year</h4>', unsafe_allow_html=True)

	products = ["Karaoke Microphones", "Disco Balls", "Spotlights", "+1 Speaker at Your Next Party", "LyxPro SPA-10 10\" Portable Professional PA Speaker (Standalone)", "Limousine Rentals", "Dave’s DJ SoundBoard: ElectroWorld X Series 9"]
	product = st.selectbox("Choose your product:", products)

	if product == "+1 Speaker at Your Next Party" or product == "LyxPro SPA-10 10\" Portable Professional PA Speaker (Standalone)":
		st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{product}</h3>', unsafe_allow_html=True)
		st.image("Speaker.png")
		st.text_input(label="", placeholder="Credit/Debit Card Number")
		st.text_input(label="", placeholder="PIN")
		st.text_input(label="", placeholder="Address")
		if st.button("Order🗒"):
			st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">Your purchase has been completed!</h3>', unsafe_allow_html=True)
	
	elif product == "Disco Balls":
		st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{product}</h3>', unsafe_allow_html=True)
		st.image("Disco_Ball.png")
		st.text_input(label="", placeholder="Credit/Debit Card Number")
		st.text_input(label="", placeholder="PIN")
		st.text_input(label="", placeholder="Address")
		if st.button("Order🗒"):
			st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">Your purchase has been completed!</h3>', unsafe_allow_html=True)
	
	elif product == "Dave’s DJ SoundBoard: ElectroWorld X Series 9":
		st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{product}</h3>', unsafe_allow_html=True)
		st.image("Soundboard.png")
		st.text_input(label="", placeholder="Credit/Debit Card Number")
		st.text_input(label="", placeholder="PIN")
		st.text_input(label="", placeholder="Address")
		if st.button("Order🗒"):
			st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">Your purchase has been completed!</h3>', unsafe_allow_html=True)
	
	elif product == "Karaoke Microphones":
		st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{product}</h3>', unsafe_allow_html=True)
		st.image("Karaoke_Microphone.jpg")
		st.text_input(label="", placeholder="Credit/Debit Card Number")
		st.text_input(label="", placeholder="PIN")
		st.text_input(label="", placeholder="Address")
		if st.button("Order🗒"):
			st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">Your purchase has been completed!</h3>', unsafe_allow_html=True)
	
	elif product == "Limousine Rentals":
		st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{product}</h3>', unsafe_allow_html=True)
		st.image("Limousine.jpg")
		st.text_input(label="", placeholder="Credit/Debit Card Number")
		st.text_input(label="", placeholder="PIN")
		st.text_input(label="", placeholder="Address")
		if st.button("Order🗒"):
			st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">Your purchase has been completed!</h3>', unsafe_allow_html=True)
	
	elif product == "Spotlights":
		st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{product}</h3>', unsafe_allow_html=True)
		st.image("Spotlight.jpg")
		st.text_input(label="", placeholder="Credit/Debit Card Number")
		st.text_input(label="", placeholder="PIN")
		st.text_input(label="", placeholder="Address")
		if st.button("Order🗒"):
			st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">Your purchase has been completed!</h3>', unsafe_allow_html=True)

elif sect == "Booking":

	st.write("Note: Events can only be booked during the current year. Call +1 (800) 229-5923 to cancel or move booked slots.")

	st.markdown(f'<h3 style="color:\'white\';font-size:20px;">Please enter the following information:</h3>', unsafe_allow_html=True)
	

	name = st.text_input(label="What's your name?", placeholder="Full Name - So I know what to call you")
	email = st.text_input(label="What's your email?", placeholder="Email (name@company.extension) - for contact information")
	cn = ""

	if "@" not in email and email != "":
		st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Invalid email address</h4>', unsafe_allow_html=True)
	else:
			
		cn = st.text_input(label="Card Number:", placeholder="Credit/Debit Card Number - for the payment")
			
		try:
			cn = int(cn)
			pin = st.text_input(label="PIN:", placeholder="PIN - for confirmation (this won't be saved)")
			loc = st.text_input(label="Address:", placeholder="Address - so I know where to be")
		
			if name != "" and email != "" and cn != "" and pin != "" and loc != "":

				t = st.selectbox("Type:", ["Party", "Wedding"])
				
				dl = [i for i in range(1, 29)]
				
				m = st.selectbox("Month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
				y = int(dt.now().strftime("%Y"))
		
				if m in ["January", "March", "May", "July", "September", "November", "December"]:
					dl += [29, 30, 31]
				elif m == "February":
					if y % 4 == 0:
						dl += [29]
				else:
					dl += [29, 30]
		
		
				d = st.selectbox("Day:", dl)
		
				apm = st.selectbox("Time Period:", ["AM", "PM"])
				dur = st.selectbox("Party Duration (Hours):", [1, 2, 3])
		
				if apm == "AM":
					if dur == 1:
						s = st.selectbox("Start time:", [7, 8, 9, 10, 11])
					if dur == 2:
						s = st.selectbox("Start time:", [7, 8, 9, 10, 11])
					if dur == 3:
						s = st.selectbox("Start time:", [7, 8, 9, 10, 11])
				
				elif apm == "PM":
					if dur == 1:
						s = st.selectbox("Start time:", [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])	
					if dur == 2:
						s = st.selectbox("Start time:", [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])	
					if dur == 3:
						s = st.selectbox("Start time:", [12, 1, 2, 3, 4, 5, 6, 7, 8, 9])	
		
				e = s+dur
		
				if e > 11 and apm == "PM":
					eapm = "AM"
				elif e > 12 and apm == "AM":
					e -= 12
					eapm = "PM"
				else:
					eapm = apm
		
				st.write(f"{t} time: {m} {d}, {y} - from {s}{apm} to {e}{eapm} (MST)")
		
				if t == "Party":
					st.write(f"Party cost: ${120*dur}")
				elif t == "Wedding":
					st.write(f"Wedding cost: ${150*dur}")
		
				submit = st.button("Book Event")
		
				if submit:
					st.markdown(f'<h3 style="color:\'0055FF\';font-size:20px;">{t} booked successfully!</h3>', unsafe_allow_html=True)
					st.write("(Reselect this section in the navigation box to book another event)")
		
		except:
			cn = str(cn)
			st.markdown(f'<h4 style="color:\'white\';font-size:18px;">Invalid card number</h4>', unsafe_allow_html=True)
			
elif sect == "About":

	st.markdown(f'<h1 style="color:#FF0000;font-size:40px;">About Dave:</h1>', unsafe_allow_html=True)
	st.markdown(f'<h5 style="color:\'green\';font-size:17px;">Dave started out playing in a rock band in college and spent 3 years as a sound engineer before changing careers. He’s been a DJ for 4 years and creates all of his own music using only the newest modern software. You might’ve even seen Dave in places like the Fortnite World Cup. It was when he\'d just hit the turning point in his career 4 months ago when Dave surpassed all DJ services as the main DJ for huge celebrations. Dave’s also an on-time, cash upfront kind of guy, so he likes to be physically present at the right times to blast some beats that everyone’s probably gonna be vibin’ to for the next month at least. He really enjoys his current career and spends most of his time jamming out to the latest hits or just vibing to some nice beats. When he isn’t, he’s usually sleeping in his room with his dog, Bruno, or enjoying some game time while listening to his latest mixes. You can contact him at discodave@musea.ca.</h5>', unsafe_allow_html=True)
	st.image("Dave_and_Bruno.jpg", caption="Dave and Bruno:")
	st.image("Fortnite_World_Cup.jpg", caption="Fortnite World Cup")
