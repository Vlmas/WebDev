import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-back-forward',
  templateUrl: './back-forward.component.html',
  styleUrls: ['./back-forward.component.css']
})
export class BackForwardComponent implements OnInit {

  constructor(private location: Location) { }

  ngOnInit(): void {
  }

  goBack() {
    this.location.back();
  }

  goForward() {
    this.location.forward();
  }
}
