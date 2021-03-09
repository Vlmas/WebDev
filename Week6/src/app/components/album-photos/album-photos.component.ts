import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Photo } from 'src/app/models/photo-obj';
import { AlbumsService } from 'src/app/services/albums.service';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {

  photos!: Photo[];
  isLoaded!: boolean;

  constructor(private albumsService: AlbumsService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getAlbumPhotos();
  }

  getAlbumPhotos() {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.isLoaded =false;
      this.albumsService.getAlbumPhotos(id).subscribe((photos) => {
        this.photos = photos;
        this.isLoaded = true;
      });
    });
  }
}
