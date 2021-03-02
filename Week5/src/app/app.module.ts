import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductItemComponent } from './components/product-item/product-item.component';
import { ProductListComponent } from './components/product-list/product-list.component';
import { TopBarComponent } from './components/top-bar/top-bar.component';
import { ProductCategoryComponent } from './components/product-category/product-category.component';
import { HomePageComponent } from './components/home-page/home-page.component';
import { ProductAlertsComponent } from './components/product-alerts/product-alerts.component';

@NgModule({
  declarations: [
    AppComponent,
    ProductItemComponent,
    ProductListComponent,
    TopBarComponent,
    ProductCategoryComponent,
    HomePageComponent,
    ProductAlertsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
