import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

apartments = [
    {"id": 1, "bedrooms": 2, "bathrooms": 1, "heater": True, "pets_allowed": False, "price": 1200, "location": "Madrid", "image_path": "./img1.jpg"},
    {"id": 2, "bedrooms": 3, "bathrooms": 2, "heater": False, "pets_allowed": True, "price": 1500, "location": "Madrid", "image_path": "./img2.jpg"},
    {"id": 3, "bedrooms": 1, "bathrooms": 1, "heater": False, "pets_allowed": True, "price": 1000, "location": "Madrid","image_path": "./img3.jpg"},
    {"id": 4, "bedrooms": 4, "bathrooms": 3, "heater": True, "pets_allowed": False, "price": 1200, "location": "Madrid","image_path": "./img4.jpg"},
    {"id": 5, "bedrooms": 5, "bathrooms": 4, "heater": True, "pets_allowed": True, "price": 1500, "location": "Madrid","image_path": "./img5.jpg"},
    {"id": 6, "bedrooms": 4, "bathrooms": 4, "heater": True, "pets_allowed": False, "price": 1300, "location": "Madrid","image_path": "./img6.jpg"},
    {"id": 7, "bedrooms": 3, "bathrooms": 3, "heater": False, "pets_allowed": True, "price": 1250, "location": "Madrid","image_path": "./img7.jpg"},
    {"id": 8, "bedrooms": 2, "bathrooms": 2, "heater": True, "pets_allowed": False, "price": 1400, "location": "Madrid","image_path": "./img8.jpg"}
]
photo = None
def filter_apartments(apts, filters):
    filtered_apartments = apts

    for key, value in filters.items():
        if value is not None:
            if key in ["min_bedrooms", "min_bathrooms"]:
                filtered_apartments = [apt for apt in filtered_apartments if apt[f"{key.split('_')[1]}"] >= value]
            elif key == "location":
                filtered_apartments = [apt for apt in filtered_apartments if apt[key] == value]
            else:
                filtered_apartments = [apt for apt in filtered_apartments if apt[key] == value]

    return filtered_apartments

def ApartmentAppGUI():
    def load_image(img_path):
        global photo
        img = Image.open(img_path)
        img = img.resize((600, 400))
        photo = ImageTk.PhotoImage(img)
        return photo

    def selection_sort_by_price(apts):
        for i in range(len(apts)):
            min_index = i
            for j in range(i + 1, len(apts)):
                if apts[j]['price'] < apts[min_index]['price']:
                    min_index = j
            apts[i], apts[min_index] = apts[min_index], apts[i]
        return apts

    def display_apartments(sorted_apartments):
        top = tk.Toplevel(root)
        top.title("All Apartments")

        canvas = tk.Canvas(top)
        canvas.pack(expand=True, fill='both')

        scrollbar = tk.Scrollbar(top, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        # Function to make the canvas scrollable
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        frame.bind('<Configure>', on_frame_configure)

        for i, apt in enumerate(sorted_apartments):
            apartment_frame = tk.Frame(frame)
            apartment_frame.grid(row=i, column=0, padx=10, pady=10)

            # Your code to display apartment details within each apartment_frame
            img = Image.open(apt['image_path'])
            img = img.resize((100, 100))  # Resize the image if needed
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(apartment_frame, image=photo)
            img_label.image = photo
            img_label.grid(row=0, column=0)

            # Display other details like price, bedrooms, etc. within the apartment_frame
            details_label = tk.Label(apartment_frame,
                                     text=f"Price: {apt['price']}\nBedrooms: {apt['bedrooms']}\nBathrooms: {apt['bathrooms']}\nLocation: {apt['location']}")
            details_label.grid(row=0, column=1)

        canvas.update_idletasks()
        canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox('all'))

    def update_preview():
        global photo
        selected_filters = {
            "min_bedrooms": int(entry_bedrooms.get()) if entry_bedrooms.get() else None,
            "min_bathrooms": int(entry_bathrooms.get()) if entry_bathrooms.get() else None,
            "heater": bool(var_heater.get()) if var_heater.get() else None,
            "pets_allowed": bool(var_pets_allowed.get()) if var_pets_allowed.get() else None,
            "location": entry_location.get() if entry_location.get() else None,
        }

        filtered = filter_apartments(apartments, selected_filters)

        if filtered:
            # Displaying the first apartment's image as a preview (you may need to handle multiple images)
            img_path = filtered[0]["image_path"]
            photo = load_image(img_path)
            label_image.config(image=photo)
            label_image.image = photo

            # Displaying the first apartment's description as a preview (you may need to handle multiple descriptions)
            apartment_description.config(text=f"Bedrooms: {filtered[0]['bedrooms']}\nBathrooms: {filtered[0]['bathrooms']}\nHeater: {filtered[0]['heater']}\nPets Allowed: {filtered[0]['pets_allowed']}\nPrice: {filtered[0]['price']}\nLocation: {filtered[0]['location']}")


        else:
            label_image.config(image="")
            label_image.image = None

        # Function to add a new apartment
    def add_apartment():
        def save_apartment():
            # Get the values from entry fields
            new_apt = {
                "id": len(apartments) + 1,
                "bedrooms": int(entry_bedrooms_new.get()),
                "bathrooms": int(entry_bathrooms_new.get()),
                "heater": var_heater_new.get(),
                "pets_allowed": var_pets_allowed_new.get(),
                "price": int(entry_price_new.get()),
                "location": entry_location_new.get(),
                "image_path": selected_image_path
            }
            apartments.append(new_apt)
            update_preview()
            top.destroy()  # Close the new window after saving the apartment

        def select_image():
            global selected_image_path
            selected_image_path = filedialog.askopenfilename()  # Open a file dialog to select an image
            label_selected_image.config(text=f"Selected Image: {selected_image_path}")

        top = tk.Toplevel(root)
        top.title("Add New Apartment")

        # Widgets for adding a new apartment
        label_add_apartment = tk.Label(top, text="Add a New Apartment", font=("Arial", 12, "bold"))
        label_add_apartment.pack()

        label_bedrooms_new = tk.Label(top, text="Bedrooms:")
        label_bedrooms_new.pack()
        entry_bedrooms_new = tk.Entry(top)
        entry_bedrooms_new.pack()

        label_bathrooms_new = tk.Label(top, text="Bathrooms:")
        label_bathrooms_new.pack()
        entry_bathrooms_new = tk.Entry(top)
        entry_bathrooms_new.pack()

        var_heater_new = tk.BooleanVar()
        checkbox_heater_new = tk.Checkbutton(top, text="Heater", variable=var_heater_new)
        checkbox_heater_new.pack()

        var_pets_allowed_new = tk.BooleanVar()
        checkbox_pets_allowed_new = tk.Checkbutton(top, text="Pets Allowed", variable=var_pets_allowed_new)
        checkbox_pets_allowed_new.pack()

        label_price_new = tk.Label(top, text="Price:")
        label_price_new.pack()
        entry_price_new = tk.Entry(top)
        entry_price_new.pack()

        label_location_new = tk.Label(top, text="Location:")
        label_location_new.pack()
        entry_location_new = tk.Entry(top)
        entry_location_new.pack()

        button_select_image = tk.Button(top, text="Select Image", command=select_image)
        button_select_image.pack()
        label_selected_image = tk.Label(top, text="Selected Image: None")
        label_selected_image.pack()

        button_save_apartment = tk.Button(top, text="Save Apartment", command=save_apartment)
        button_save_apartment.pack()


    # GUI setup
    root = tk.Tk()
    root.title("Apartment Search")
    root.geometry("1960x1080")

    # Filters
    label_bedrooms = tk.Label(root, text="Minimum Bedrooms:")
    label_bedrooms.pack()
    entry_bedrooms = tk.Entry(root)
    entry_bedrooms.pack()

    label_bathrooms = tk.Label(root, text="Minimum Bathrooms:")
    label_bathrooms.pack()
    entry_bathrooms = tk.Entry(root)
    entry_bathrooms.pack()

    var_heater = tk.BooleanVar()
    checkbox_heater = tk.Checkbutton(root, text="Heater", variable=var_heater)
    checkbox_heater.pack()

    var_pets_allowed = tk.BooleanVar()
    checkbox_pets_allowed = tk.Checkbutton(root, text="Pets Allowed", variable=var_pets_allowed)
    checkbox_pets_allowed.pack()

    label_location = tk.Label(root, text="Location:")
    label_location.pack()
    entry_location = tk.Entry(root)
    entry_location.pack()

    button_search = tk.Button(root, text="Search", command=update_preview)
    button_search.pack()

    label_image = tk.Label(root)
    label_image.pack()

    apartment_description = tk.Label(root, text="", wraplength=300)  # Adjust wraplength as needed
    apartment_description.pack()

    button_add_apartment = tk.Button(root, text="Add Apartment", command=add_apartment)
    button_add_apartment.pack()

    button_display_apartments = tk.Button(root, text="Display Apartments", command=lambda: display_apartments(selection_sort_by_price(apartments)))
    button_display_apartments.pack()

    root.mainloop()

if __name__ == "__main__":
    ApartmentAppGUI()
