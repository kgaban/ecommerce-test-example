import logging
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def test_add_to_cart_and_remove():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        try:
            # Navigate to the local ecommerce website
            url = 'http://localhost:5000'
            logging.info(f'Navigating to {url}')
            page.goto(url)

            # Wait for the product list to be loaded
            logging.info('Waiting for product list to load')
            page.wait_for_selector('#product-1')

            # Click the "Add to Cart" button for Product 1
            logging.info('Clicking "Add to Cart" button')
            page.click('#product-1 button[type="submit"]')

            # Wait for the cart page to load
            logging.info('Waiting for cart page to load')
            page.wait_for_selector('.cart-item-name')

            # Verify the item is added to the cart
            cart_item_name = page.inner_text('.cart-item-name')
            assert "Product 1" in cart_item_name  # Adjust with actual product name
            logging.info(f'Item added to cart: {cart_item_name}')

            # Remove the item from the cart
            logging.info('Removing item from cart')
            page.click('button:has-text("Remove from Cart")')

            # Wait for the cart to update
            logging.info('Waiting for cart to update')
            page.wait_for_selector('.cart-item-name', state='hidden')

            # Verify the item is removed from the cart
            cart_items = page.query_selector_all('.cart-item-name')
            assert not any("Product 1" in item.inner_text()
                           for item in cart_items)
            logging.info('Item successfully removed from cart')

        except Exception as e:
            logging.error(f'Error occurred: {str(e)}')

        finally:
            # Close the browser
            browser.close()
            logging.info('Browser closed')


if __name__ == "__main__":
    test_add_to_cart_and_remove()
