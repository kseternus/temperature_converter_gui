import customtkinter

# GUI temperature converter with customtkinter*
# * pip install customtkinter
# It ain't much, but it's honest work


# Function that take values from Entry field, value from selected combo boxes (selected temp unit and wanted
# output temp unit) then calculate output and set it in output label. :)
def convert():
    temperature = enter_temperature.get()
    enter_unit = combo_scale_unit.get()
    output_unit = combo_unit_select.get()
    if enter_unit == output_unit[0] and enter_unit == 'K':
        output_str.set(f'{temperature} K')
    elif enter_unit == output_unit[0]:
        output_str.set(f'{temperature}° {enter_unit}')
    elif enter_unit == 'C':
        if output_unit[0] == 'F':
            output_str.set(f'{(float(temperature)*(9/5)+32):.2f} °{output_unit[0]}')
        else:
            output_str.set(f'{(float(temperature) + 273.15):.2f} {output_unit[0]}')
    elif enter_unit == 'F':
        if output_unit[0] == 'C':
            output_str.set(f'{((float(temperature)-32)/1.8):.2f} °{output_unit[0]}')
        else:
            output_str.set(f'{((float(temperature)-32)/1.8 + 273.15):.2f} {output_unit[0]}')
    elif enter_unit == 'K':
        if output_unit[0] == 'C':
            output_str.set(f'{(float(temperature) - 273.15):.2f} °{output_unit[0]}')
        else:
            output_str.set(f'{((float(temperature) - 273.15) * 1.8 +32):.2f} °{output_unit[0]}')


# Create main window
root = customtkinter.CTk()
root.title('Temperature converter')
root.geometry('1200x600')
root.resizable(False, False)
root.config(background='#aa6f73')


# Create main left frame with will be split in three frames stacked vertically
left_main_frame = customtkinter.CTkFrame(root, width=500, height=600, corner_radius=0, fg_color='#66545e')
left_main_frame.pack(side='left', fill='y')

# Create frame no1
frame1 = customtkinter.CTkFrame(left_main_frame, width=500, height=200, fg_color='#66545e')
frame1.pack(fill='x')

# Create title and info about entering temp
# Title
title = customtkinter.CTkLabel(frame1,
                               text='Temperature converter',
                               fg_color='#66545e',
                               font=('Futura', 32))
# Enter temp text
enter_label_unit = customtkinter.CTkLabel(frame1,
                                          text='Enter temperature:',
                                          fg_color='#66545e',
                                          font=('Futura', 16))
title.pack(anchor='w', padx=20, pady=(60, 60), expand=True)
enter_label_unit.pack(anchor='w', padx=20)

# Create frame no2
frame2 = customtkinter.CTkFrame(left_main_frame, width=500, height=200, fg_color='#66545e')
frame2.pack(fill='x')

# Create entry where user enter temperature value to convert
# Entry field
enter_temperature = customtkinter.CTkEntry(frame2,
                                           border_width=0,
                                           corner_radius=0,
                                           width=350,
                                           height=40,
                                           fg_color='#a39193',
                                           font=('Futura', 16))

# Create combobox where user select entered temperature unit
combo_scale_unit = customtkinter.CTkComboBox(frame2,
                                             border_width=0,
                                             corner_radius=0,
                                             width=40,
                                             height=40,
                                             fg_color='#aa6f73',
                                             button_color='#aa6f73',
                                             dropdown_fg_color='#aa6f73',
                                             state='readonly',
                                             values=['K', 'C', 'F'])
enter_temperature.place()
enter_temperature.pack(side='left', padx=(20, 0), pady=(0, 120), anchor='center')
combo_scale_unit.set('K')
combo_scale_unit.pack(side='left', pady=(0, 120), anchor='center')

# Create frame no3
frame3 = customtkinter.CTkFrame(left_main_frame, width=500, height=200, fg_color='#66545e')
frame3.pack(fill='x')

# Select output text
output_unit_label = customtkinter.CTkLabel(frame3,
                                           text='Select output',
                                           fg_color='#66545e',
                                           font=('Futura', 16))
# Create combobox where user select wanted output temperature unit
combo_unit_select = customtkinter.CTkComboBox(frame3,
                                              border_width=0,
                                              corner_radius=0,
                                              width=400,
                                              height=40,
                                              fg_color='#a39193',
                                              button_color='#a39193',
                                              dropdown_fg_color='#a39193',
                                              state='readonly',
                                              values=['Kelvin', 'Celsius', 'Fahrenheit'])
# Button that make magic
convert_button = customtkinter.CTkButton(frame3,
                                         border_width=0,
                                         corner_radius=0,
                                         width=150,
                                         height=50,
                                         text='Convert',
                                         fg_color='#a39193',
                                         hover_color='#aa6f73',
                                         command=convert)
output_unit_label.pack(anchor='w', padx=20)
combo_unit_select.set('Celsius')
combo_unit_select.pack(anchor='w', padx=20)
convert_button.pack(pady=(80, 0))

# Create the right frame
right_frame = customtkinter.CTkFrame(root, width=700, height=600, corner_radius=0, fg_color='#aa6f73')
right_frame.pack(fill='x')
# variable that put value from function into text field in output label
output_str = customtkinter.StringVar()
output = customtkinter.CTkLabel(right_frame, text='1234', font=('Futura', 100), textvariable=output_str)

output.pack(pady=(240, 0))


# Run the main window's event loop
root.mainloop()
