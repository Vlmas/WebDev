import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.css']
})

export class CarComponent implements OnInit {
  brand:string;
  model: string;
  topSpeed: number;
  colors: Colors;
  features: string[];

  constructor() { 
    this.brand='Toyota';
    this.model='Camry';
    this.topSpeed=210.5;
    this.features=['abs','autopilot','rear-camera'];
    this.colors={
      exterior: 'white' ,
      interior: 'black'
    };
  }

  ngOnInit(): void {}

  getFeatures(): string {
    return `${this.features[0]}, ${this.features[1]}, ${this.features[2]}`;
  }

  toySelect(): void {
    this.brand='Toyota';
    this.model='Camry';
    this.topSpeed=210.5;
    this.features=['abs','autopilot','rear-camera'];
    this.colors={
      exterior: 'white' ,
      interior: 'black'
    };
  }

  lexSelect(): void {
    this.brand='Lexus';
    this.model='ES350';
    this.topSpeed=225.3;
    this.features=['abs','autopilot','rear-camera'];
    this.colors={
      exterior: 'white',
      interior: 'black'
    };
  }

  hyuSelect(): void {
    this.brand='Hyundai';
    this.model='Grandeur';
    this.topSpeed=215.3;
    this.features=['abs','autopilot','rear-camera'];
    this.colors={
      exterior: 'white',
      interior: 'black'
    };
  }
}

interface Colors {
  exterior: string,
  interior: string
}