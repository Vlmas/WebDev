import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';
import { ProductItem } from 'src/app/product-item';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  showDescription: boolean = false;
  flagButtonText: string = 'show description';
  showShare: boolean = false;
  
  @Output() status = new EventEmitter<any>();
  @Input() product!: ProductItem;

  constructor() { }

  ngOnInit(): void {
  }

  swapDescriptionFlag() {
    this.showDescription = !this.showDescription;
    this.flagButtonText = (this.flagButtonText === 'show description')?'hide description':'show description';
  }

  changeToShow() {
    this.showShare = !this.showShare;
  }

  share(viaWhat: string, link: string) {
    if(viaWhat === 'telegram') {
      open('https://t.me/share/url?url=Product+on+Amazon&text='+link);
    }
    else if(viaWhat === 'whatsapp') {
      open('https://wa.me/123456789/?text='+link);
    }
  }

  incrementLikes() {
    this.product.likes++;
  }

  deleteNode(value: number) {
    this.status.emit(value);
  }
}