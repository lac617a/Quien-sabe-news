/**
 * @license Copyright (c) 2003-2020, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.extraPlugins = 'Youtube';
	config.youtube_width = '728';
	config.youtube_height = '480';
	config.youtube_responsive = true;
	config.enterMode = CKEDITOR.ENTER_BR;
	config.youtube_controls = true;
	config.youtube_related = true;
};
