from selenium.webdriver.common.by import By


class PetsPageLocators(object):
    petsMainButton = (By.ID, "menu")
    petsFindPetButton = (By.ID, "menu__search")
    petsAddANewViewButton = (By.ID, "menu__add-view")
    petsCardViewButton = (By.ID, "view-menu__card")
    petsAppCardView = (By.ID, "view__card-view")
    petsItemsPerPageMatSelect = (By.CSS_SELECTOR, 'mat-select[aria-label="Items per page:"]')
    pets50ItemPerPageMatOption = (By.CSS_SELECTOR, "mat-option:nth-child(4)")
    petsTableViewStatusTd = (By.ID, "pet-row__status")
    petsTableViewNameTd = (By.ID, "pet-row__name")
    petsNameMatCardTitle = (By.ID, "pet-card__name")

    petsSelectAttributeMatSelect = (By.ID, "attribute__select")
    petsStatusAttributeMatOption = (By.ID, "select__status")
    petsNextButton = (By.CSS_SELECTOR, 'button[type="submit"]')
    petsStatusSelectMatOption = (By.ID, "status__select")
    petsSoldStatusMatOption = (By.ID, "select__sold")
    petsSearchButton = (By.ID, "actions__search")




