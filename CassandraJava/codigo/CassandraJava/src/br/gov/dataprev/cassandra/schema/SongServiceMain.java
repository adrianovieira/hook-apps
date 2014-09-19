package br.gov.dataprev.cassandra.schema;

import java.util.UUID;

public class SongServiceMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		//Cria o keyspace com as column families
		CriacaoSchema cs = new CriacaoSchema();
		cs.createKeyspace();	
		cs.createColumnFamilies();
		cs.close();
		
		//persiste uma musica na column family song_service.songs
		SongDAO songdao = new SongDAO();
		UUID song_id = UUID.randomUUID();
		String title = "Beijinho no Ombro";
		String album = "Qualquer Coisa";
		String artist = "Valesca Popozuda";
		songdao.saveSong(song_id,title, album, artist);
		songdao.close();
		
		//persiste uma playlista na column family song_service.playlists
		PlaylistsDAO playlistdao = new PlaylistsDAO();
		UUID playlist_id = UUID.randomUUID();		
		playlistdao.savePlaylist(0, song_id, title, album, artist);
		playlistdao.close();
		
		
	}

}
