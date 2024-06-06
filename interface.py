from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
import app

class SimpleUIApp(App):
    def build(self):
        # Create the main layout using BoxLayout
        main_layout = BoxLayout(orientation='vertical', spacing=20, padding=100)
        
        # Create a Spinner with values from 1 to 10
        spinner = Spinner(
            text='5',
            values=[str(i) for i in range(1, 11)],
            size_hint=(None, None),
            size=(250, 50),
        )
        
        # Create a Label to display the selected value
        selected_label = Label(text='Tickets: ')

        # Bind the spinner selection to a function
        spinner.bind(text=lambda instance, value: setattr(selected_label, 'text', 'Tickets: ' + value))
        
        
        
        # Create text labels
        label1 = Label(text='Welcome to HybridBot, I will help you to buy tickets!')
        label2 = Label(text='Enter your email:')
        
        # Create a email input field
        email_input = TextInput(text="kristoffer.seyffarth@gmail.com")
        link_input = TextInput(text="https://www.uka.no/program/817-oktoberfest/1123/")
        card_number_input=TextInput(text="4569971025493575")
        expire_date_input=TextInput(text="10/23")
        cvc_input=TextInput(text="831")
        name_input=TextInput(text="kristoffer seyffarth")
        
        # Create buttons
        button1 = Button(text='Click Me')
        
        # Bind button clicks to functions
        button1.bind(on_press=self.on_button1_click)
        
        # Add widgets to the main layout
        main_layout.add_widget(selected_label)
        main_layout.add_widget(spinner)
        main_layout.add_widget(label1)
        main_layout.add_widget(label2)
        main_layout.add_widget(link_input)
        main_layout.add_widget(email_input)
        main_layout.add_widget(card_number_input)
        main_layout.add_widget(expire_date_input)
        main_layout.add_widget(cvc_input)
        main_layout.add_widget(name_input)
        main_layout.add_widget(button1)
        
        return main_layout
    
    def on_button1_click(self, instance):
        amount = self.root.children[9].text
        email = self.root.children[5].text
        link  = self.root.children[6].text
        card_number = self.root.children[4].text
        expire_date= self.root.children[3].text
        cvc= self.root.children[2].text
        name= self.root.children[1].text
        
        print("you want to buy " + amount + " tickets on email: " + email + "for link " + link + "")
        app.main(email,amount,link,card_number,expire_date,cvc,name)

if __name__ == '__main__':
    SimpleUIApp().run()