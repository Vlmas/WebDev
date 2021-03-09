import { Component, OnInit } from '@angular/core';
import { Album } from 'src/app/models/album-obj';
import { AlbumsService } from 'src/app/services/albums.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {

  albums!: Album[];
  isLoaded!: boolean;
  newContent: string;
  randomImage: string;

  constructor(private albumsService: AlbumsService) {
    this.newContent = '';
    this.randomImage = 'https://cdn1.iconfinder.com/data/icons/love-wedding-vol-2/512/wedding_song_music_album-128.png';
  }

  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums() {
    this.isLoaded = false;
    this.albumsService.getAlbums().subscribe((albums) => {
      this.albums = albums;
      this.isLoaded = true;
    });
  }

  deleteAlbum(id: number) {
    this.albums = this.albums.filter((a) => a.id !== id);
    this.albumsService.deleteAlbum(id).subscribe(() => {
      console.log('deleted');
    });
  }

  addAlbum() {
    this.isLoaded =false;
    this.albumsService.addAlbum({title: this.newContent} as Album).subscribe((album) => {
      this.albums.push(album);
      this.isLoaded = true;
      this.newContent = '';
    });
  }
}
