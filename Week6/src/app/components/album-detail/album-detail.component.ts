import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Album } from 'src/app/models/album-obj';
import { AlbumsService } from 'src/app/services/albums.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {

  album!: Album;
  isLoaded!: boolean;

  constructor(private route: ActivatedRoute, private albumsService: AlbumsService) { }

  ngOnInit(): void {
    this.getPost();
  }

  getPost() {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.isLoaded = false;
      this.albumsService.getAlbum(id).subscribe((album) => {
        this.album = album;
        this.isLoaded = true;
      });
    });
  }

  updateAlbum() {
    this.isLoaded = false;
    this.albumsService.updateAlbum(this.album).subscribe((post) => {
      this.isLoaded = true;
    });
  }
}