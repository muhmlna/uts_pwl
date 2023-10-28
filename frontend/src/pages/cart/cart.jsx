import React, { useContext } from "react";
import { ShopContext } from "../../context/shop-context";
import "./cart.css";
import { CartItem } from "./cart-item";
import { useNavigate } from "react-router-dom";
import { backendUrl } from "../../env";
const getProducts = async () => {
  const response = await fetch(`${backendUrl}`);
  const data = await response.json();

  return data.data;
};

export const Cart = () => {
  const { cartItems, getTotalCartAmount, checkout } = useContext(ShopContext);
  const totalAmount = getTotalCartAmount();

  const [PRODUCTS, setProducts] = React.useState([]);
  const navigate = useNavigate();
  const productIds = Object.keys(cartItems).find((item) => cartItems[item] > 0);

  React.useEffect(() => {
    getProducts().then((data) => setProducts(data));
  }, []);

  return (
    <div className="cart">
      <div>
        <h1>Your Cart Items {typeof totalAmount}</h1>
      </div>
      <div className="cart">
        {PRODUCTS.map((product) => {
          if (cartItems[product.id] !== 0) {
            return (
              <CartItem
                data={{
                  id: product.id,
                  productName: product.name,
                  price: product.price,
                  productImage: product.image_url,
                }}
              />
            );
          }
        })}
      </div>

      {totalAmount > 0 ? (
        <div className="checkout">
          <p> Subtotal: ${totalAmount} </p>
          <button onClick={() => navigate("/")}> Continue Shopping </button>
          <button
            onClick={() => {
              checkout();
              navigate("/checkout");
            }}
          >
            {" "}
            Checkout{" "}
          </button>
        </div>
      ) : (
        <h1> Your Shopping Cart is Empty</h1>
      )}
    </div>
  );
};
