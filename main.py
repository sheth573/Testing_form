import flet as ft
from flet import *


def main(page:ft.Page):
    page.title = "Testing-Form"
    page.horizontal_alignment = "center"
    page.padding = 100
    
    input_name = ft.TextField(hint_text="Full Name")
    input_age = ft.TextField(hint_text="Age")
    input_mobile = ft.TextField(hint_text="Mobile Number")
    print_details = ft.Column()
    
    
    def save_click(e):
        if not input_name.value and input_age and input_mobile:
            input_name.error_text="Please Type Your Name..."
            input_age.error_text="Please Type Your Correct Age..."
            input_mobile.error_text="Please Type Your Mobile Number..."
            page.update() 
        else:
            page.controls.clear()
            print_details.controls.append(ft.Text(f"Welcome Mr.{input_name.value} Your Age is {input_age.value} and Your Mobile Number is {input_mobile.value}"))
            page.add(print_details)    
    page.add(
        
            input_name,
            input_age,
            input_mobile,
            ft.TextButton("Save in Preview", icons.SAVE, on_click=save_click))
# Run the application
ft.app(target=main)
