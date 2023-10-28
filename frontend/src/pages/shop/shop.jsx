import React from "react";
import { PRODUCTS } from "../../products";
import { Product } from "./product";
import { backendUrl } from "../../env";
import "./shop.css";

const getProducts = async () => {
  const response = await fetch(`${backendUrl}`);
  const data = await response.json();
  
  return data.data;
};

export const Shop = () => {
  const [products, setProducts] = React.useState([]);

  React.useEffect(() => {
    getProducts().then((data) => setProducts(data));
  }, []);

  return (
    <div className="shop">
      <div className="shopTitle">
        <h1>ULS SHOP</h1>
      </div>

      <div className="products">
        {products.map((product) => (
          <Product data={{
            id: product.id,
            productName: product.name,
            price: product.price,
            productImage: product.image_url,
          }} />
        ))}
      </div>
    </div>
  );
};
