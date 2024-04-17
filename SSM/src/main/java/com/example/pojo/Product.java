package com.example.pojo;

import java.math.BigDecimal;

public class Product {
    private Integer productId;
    private String productName;
    private String description;
    private boolean sub;
    private BigDecimal newPrice;
    private BigDecimal oldPrice;
    private String src;

    public Integer getProductId() {
        return productId;
    }

    public void setProductId(Integer productId) {
        this.productId = productId;
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public boolean isSub() {
        return sub;
    }

    public void setSub(boolean sub) {
        this.sub = sub;
    }

    public BigDecimal getNewPrice() {
        return newPrice;
    }

    public void setNewPrice(BigDecimal newPrice) {
        this.newPrice = newPrice;
    }

    public BigDecimal getOldPrice() {
        return oldPrice;
    }

    public void setOldPrice(BigDecimal oldPrice) {
        this.oldPrice = oldPrice;
    }

    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }

    public Product(Integer productId, String productName, String description, boolean sub, BigDecimal newPrice, BigDecimal oldPrice, String src) {
        this.productId = productId;
        this.productName = productName;
        this.description = description;
        this.sub = sub;
        this.newPrice = newPrice;
        this.oldPrice = oldPrice;
        this.src = src;
    }

    @Override
    public String toString() {
        return "Product{" +
                "productId=" + productId +
                ", productName='" + productName + '\'' +
                ", description='" + description + '\'' +
                ", sub=" + sub +
                ", newPrice=" + newPrice +
                ", oldPrice=" + oldPrice +
                ", src='" + src + '\'' +
                '}';
    }
}
