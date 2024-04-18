import os
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from read_properties import read_properties


class HomePage:
    def __init__(self, driver, environment):
        self.driver = driver
        self.url = read_properties("urls.properties", environment)

    def load(self):
        """Carga la página."""
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("Error al cargar la página:", e)

    def home_page_is_displayed(self):
        """Verifica que la página de inicio esté cargada."""
        try:
            self.header_is_displayed()
            self.footer_is_displayed()
        except Exception as e:
            print("Error al verificar la página de inicio:", e)

    def footer_is_displayed(self):
        """Verifica que el pie de página esté visible."""
        try:
            footer = self.driver.find_element(By.XPATH, "//div[@class=' footer_top_agile_w3ls gffoot footer_style']")
            elements = footer.find_elements(By.XPATH, ".//li//a")
            for element in elements:
                assert element.text, "El elemento no tiene texto"
        except NoSuchElementException as e:
            print("Error al verificar el pie de página:", e)

    def header_is_displayed(self):
        """Verifica que el encabezado esté visible."""
        try:
            header = self.driver.find_element(By.XPATH, "//header[@class='jumbotron text-center header_style']")
            elements = header.find_elements(By.XPATH, ".//a")
            for element in elements:
                href = element.get_attribute("href")
                assert href, "El elemento no tiene el atributo href"
        except NoSuchElementException as e:
            print("Error al verificar el encabezado:", e)

    def enter_credentials(self, email, password):
        """EL BOTON DE LOGIN NO FUNCIONA"""

    def suggestion_input(self, input_value):
        try:
            suggestion_input = self.driver.find_element(By.XPATH, "//input[@id='autocomplete']")
            suggestion_input.send_keys(input_value)
        except NoSuchElementException as e:
            print("Error al verificar el encabezado:", e)

    def suggestion_list_is_displayed(self, check_visibility=True):
        try:
            suggestion_input = self.driver.find_element(By.XPATH, "//ul[@class='ui-menu ui-widget ui-widget-content "
                                                                  "ui-autocomplete ui-front']")
            elements = suggestion_input.find_elements(By.XPATH, ".//li")

            if check_visibility:
                assert len(elements) >= 0, "La lista de sugerencias no está vacía"
            else:
                assert len(elements) == 0, "La lista de sugerencias está vacía"

        except NoSuchElementException as e:
            print("Error al verificar la lista de sugerencias:", e)

    def suggestion_list_contains_expected_country(self, country):
        try:
            suggestion_list = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//ul[@class='ui-menu ui-widget ui-widget-content ui-autocomplete ui-front']"))
            )
            elements = suggestion_list.find_elements(By.XPATH, ".//li//div")
            country_found = False
            for element in elements:
                if country in element.text:
                    country_found = True
                    break

            assert country_found, f"No se encontró el país '{country}' en la lista de sugerencias"
        except NoSuchElementException as e:
            print("Error al verificar la lista de sugerencias:", e)

    def select_country_from_suggestions(self, country):
        try:
            # Espera a que la lista de sugerencias esté presente y visible
            suggestion_list = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//ul[@class='ui-menu ui-widget ui-widget-content ui-autocomplete ui-front']"))
            )
            elements = suggestion_list.find_elements(By.XPATH, ".//li//div")
            country_found = False
            for element in elements:
                if country in element.text:
                    element.click()
                    country_found = True
                    break

            assert country_found, f"No se encontró el país '{country}' en la lista de sugerencias"
        except NoSuchElementException as e:
            print("Error al seleccionar el país de la lista de sugerencias:", e)

    def verify_input_contains_selected_country(self, country):
        try:
            input_field = self.driver.find_element(By.XPATH, "//input[@id='autocomplete']")
            assert country in input_field.get_attribute(
                "value"), f"El campo de entrada no contiene el país '{country}' seleccionado"
        except NoSuchElementException as e:
            print("Error al verificar el campo de entrada:", e)

    def clear_input_field(self):
        try:
            input_field = self.driver.find_element(By.XPATH, "//input[@id='autocomplete']")
            input_field.clear()
        except NoSuchElementException as e:
            print("Error al limpiar el campo de entrada:", e)

    def verify_input_field_empty(self):
        try:
            input_field = self.driver.find_element(By.XPATH, "//input[@id='autocomplete']")
            assert input_field.get_attribute("value") == "", "El campo de entrada no está vacío"
        except NoSuchElementException as e:
            print("Error al verificar el campo de entrada:", e)

    def example_dropdown_select_option(self, option):
        try:
            example_dropdown = self.driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
            select = Select(example_dropdown)
            select.select_by_visible_text(option)
        except NoSuchElementException as e:
            print("Error al verificar el dropdown:", e)

    def verify_dropdown_has_selected_option(self, expected_option):
        try:
            example_dropdown = self.driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
            select = Select(example_dropdown)
            selected_option = select.first_selected_option
            assert selected_option.text == expected_option, (f"La opción seleccionada no es '{expected_option}', se "
                                                             f"encontró '{selected_option.text}'")
        except NoSuchElementException as e:
            print("Error al verificar el dropdown:", e)

    def click_open_window_button(self):
        try:
            current_window_handle = self.driver.current_window_handle
            open_window_button = self.driver.find_element(By.XPATH, "//button[@id='openwindow']")
            open_window_button.click()
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            all_window_handles = self.driver.window_handles
            new_window_handle = [handle for handle in all_window_handles if handle != current_window_handle][0]
            assert new_window_handle, "No se abrió una nueva ventana después de hacer clic en el botón"
            self.driver.switch_to.window(new_window_handle)
        except NoSuchElementException as e:
            print("Error al verificar el botón de abrir ventana:", e)

    def find_element_in_new_window(self, text):
        try:
            current_window_handle = self.driver.current_window_handle
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            all_window_handles = self.driver.window_handles
            new_window_handle = [handle for handle in all_window_handles if handle != current_window_handle][0]
            self.driver.switch_to.window(new_window_handle)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
            )
            return element
        except TimeoutException:
            raise AssertionError(f"El texto '{text}' no está presente en la nueva ventana.")
        except NoSuchElementException as e:
            print("Error al buscar el elemento en la nueva ventana:", e)

    def click_open_tab_button(self):
        try:
            current_tabs_count = len(self.driver.window_handles)
            open_tab_button = self.driver.find_element(By.XPATH, "//fieldset//a[@id='opentab']")
            open_tab_button.click()
            WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > current_tabs_count)
            assert len(
                self.driver.window_handles) == current_tabs_count + 1, ("No se ha abierto una nueva pestaña después de "
                                                                        "hacer clic en el botón")
            self.driver.switch_to.window(self.driver.window_handles[-1])

        except NoSuchElementException as e:
            print("Error al verificar el botón de abrir pestaña:", e)
        except TimeoutException:
            raise AssertionError("No se ha abierto una nueva pestaña después de hacer clic en el botón")

    def verify_button_in_new_tab(self, scenario_name):
        try:
            first_window_handle = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[-1])
            button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@class='btn btn-primary view-all-courses-btn']"))
            )
            assert button.is_displayed(), "El botón no está presente en la nueva pestaña"
            screenshots_folder = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshots_folder):
                os.makedirs(screenshots_folder)
            screenshot_path = os.path.join(screenshots_folder, f"{scenario_name}.png")
            self.driver.save_screenshot(screenshot_path)
            self.driver.switch_to.window(first_window_handle)

        except TimeoutException:
            error_message = "El botón no está presente en la nueva pestaña"
            print(error_message)
            screenshots_folder = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshots_folder):
                os.makedirs(screenshots_folder)
            screenshot_path = os.path.join(screenshots_folder, f"{scenario_name}.png")
            self.driver.save_screenshot(screenshot_path)
            raise AssertionError(error_message)
        except AssertionError as e:
            print("Error al verificar el botón en la nueva pestaña:", e)
            screenshots_folder = os.path.join(os.getcwd(), "screenshots")
            if not os.path.exists(screenshots_folder):
                os.makedirs(screenshots_folder)
            screenshot_path = os.path.join(screenshots_folder, f"{scenario_name}.png")
            self.driver.save_screenshot(screenshot_path)
            raise e

    def input_text_for_dialog(self, text, btn_type):
        try:
            alert_text_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']")
            alert_text_input.send_keys(text)
            if btn_type == "alert":
                self.driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
            else:
                self.driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
        except NoSuchElementException as e:
            print("Error", e)

    def print_alert_text(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Texto en la alerta:", alert.text)
        except NoSuchElementException as e:
            print("Error al verificar el botón de abrir dialogo:", e)

    def expected_text_for_dialog(self, expected_text):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            assert alert_text == expected_text, "El texto en la alerta no coincide con el texto esperado."
            alert.accept()

        except NoSuchElementException as e:
            print("Error al verificar el botón de abrir dialogo:", e)

    def print_courses_by_price(self, price):
        try:
            course_rows = self.driver.find_elements(By.XPATH,
                                                    "//table[@name='courses']//tr[td[text()='" + price + "']]")
            print("Se encontraron " + str(len(course_rows)) + " cursos con precio de $" + price)
            for course_row in course_rows:
                course_details = course_row.find_elements(By.XPATH, ".//preceding-sibling::td")
                if len(course_details) >= 3:
                    print("Nombre del profesor:", course_details[0].text)
                    print("Nombre del curso:", course_details[1].text)
                    print("-" * 20)
                else:
                    print("No se encontraron suficientes detalles para imprimir")
        except NoSuchElementException as e:
            print("Error: Elemento no encontrado -", e)

    def print_people_info_by_position(self, position):
        try:
            people_rows = self.driver.find_elements(By.XPATH,
                                                    "//table[@id='product']//tr[td[text()='" + position + "']]")
            print("Se encontraron " + str(len(people_rows)) + " personas con la posición de " + position)
            for people_row in people_rows:
                people_details = people_row.find_elements(By.XPATH, ".//preceding-sibling::td")
                if len(people_details) >= 3:
                    print("Nombre:", people_details[0].text)
                    print("Ciudad:", people_details[2].text)
                    print("-" * 20)
                else:
                    print("No se encontraron suficientes detalles para imprimir")
        except NoSuchElementException as e:
            print("Error: Elemento no encontrado -", e)

    def switch_to_courses_iframe(self):
        try:
            iframe = WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "courses-iframe")))

            print("Cambió correctamente al iframe con ID 'courses-iframe'")
        except TimeoutException:
            print("Error: No se pudo cambiar al iframe con ID 'courses-iframe'")

    def print_odd_elements_in_iframe(self):
        try:
            div_elements = self.driver.find_elements(By.XPATH,
                                                     "//div[@class='list-column col-md-6 col-sm-6 col-xs-12']//ul//li")
            for index, div_element in enumerate(div_elements):
                if index % 2 != 0:
                    print("Odd:", div_element.text)
        except TimeoutException:
            print("Error: No se pudo encontrar el iframe o el elemento dentro del iframe")
        finally:
            self.driver.switch_to.default_content()
