import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Product, products  } from '../../productitem'

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products: Product[] = products;

  constructor() { }

  ngOnInit(): void { }

  share(id: number) {
    let idx = this.products.findIndex(p => p.id === id);
    open('https://t.me/share/url?url=Product+from+Amazon&text='+this.products[idx].shareLink);
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}
