/**
 * @fileoverview gRPC-Web generated client stub for 
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!



const grpc = {};
grpc.web = require('grpc-web');

const proto = require('./tile_server_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.TileServerClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

  /**
   * @private @const {?Object} The credentials to be used to connect
   *    to the server
   */
  this.credentials_ = credentials;

  /**
   * @private @const {?Object} Options for the client
   */
  this.options_ = options;
};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.TileServerPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

  /**
   * @private @const {?Object} The credentials to be used to connect
   *    to the server
   */
  this.credentials_ = credentials;

  /**
   * @private @const {?Object} Options for the client
   */
  this.options_ = options;
};


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.TileXYZ,
 *   !proto.Tile>}
 */
const methodInfo_TileServer_GetTile = new grpc.web.AbstractClientBase.MethodInfo(
  proto.Tile,
  /** @param {!proto.TileXYZ} request */
  function(request) {
    return request.serializeBinary();
  },
  proto.Tile.deserializeBinary
);


/**
 * @param {!proto.TileXYZ} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.Tile)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.Tile>|undefined}
 *     The XHR Node Readable Stream
 */
proto.TileServerClient.prototype.getTile =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/TileServer/GetTile',
      request,
      metadata || {},
      methodInfo_TileServer_GetTile,
      callback);
};


/**
 * @param {!proto.TileXYZ} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.Tile>}
 *     A native promise that resolves to the response
 */
proto.TileServerPromiseClient.prototype.getTile =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/TileServer/GetTile',
      request,
      metadata || {},
      methodInfo_TileServer_GetTile);
};


module.exports = proto;

