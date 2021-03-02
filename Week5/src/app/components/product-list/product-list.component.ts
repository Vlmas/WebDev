import { Component, Input, OnInit } from '@angular/core';
import { ProductItem } from 'src/app/product-item';
import { ActivatedRoute } from '@angular/router';
import { products } from '../../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products!: ProductItem[];
 
  constructor(public route: ActivatedRoute) { }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    const productIdFromRoute = String(routeParams.get('productId'));
    this.products = products.filter(product => product.productId === productIdFromRoute);
  }

  editProducts(id: number) {
    let idx = this.products.findIndex(p => p.id === id);
    this.products.splice(idx, 1);
  }
}