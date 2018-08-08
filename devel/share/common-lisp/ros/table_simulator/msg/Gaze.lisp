; Auto-generated. Do not edit!


(cl:in-package table_simulator-msg)


;//! \htmlinclude Gaze.msg.html

(cl:defclass <Gaze> (roslisp-msg-protocol:ros-message)
  ((offset
    :reader offset
    :initarg :offset
    :type cl:float
    :initform 0.0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass Gaze (<Gaze>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Gaze>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Gaze)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name table_simulator-msg:<Gaze> is deprecated: use table_simulator-msg:Gaze instead.")))

(cl:ensure-generic-function 'offset-val :lambda-list '(m))
(cl:defmethod offset-val ((m <Gaze>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:offset-val is deprecated.  Use table_simulator-msg:offset instead.")
  (offset m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <Gaze>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:distance-val is deprecated.  Use table_simulator-msg:distance instead.")
  (distance m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <Gaze>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:angle-val is deprecated.  Use table_simulator-msg:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Gaze>) ostream)
  "Serializes a message object of type '<Gaze>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'offset))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Gaze>) istream)
  "Deserializes a message object of type '<Gaze>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'offset) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Gaze>)))
  "Returns string type for a message object of type '<Gaze>"
  "table_simulator/Gaze")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Gaze)))
  "Returns string type for a message object of type 'Gaze"
  "table_simulator/Gaze")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Gaze>)))
  "Returns md5sum for a message object of type '<Gaze>"
  "7c58cf575410a1c3851d426cf912c3a4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Gaze)))
  "Returns md5sum for a message object of type 'Gaze"
  "7c58cf575410a1c3851d426cf912c3a4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Gaze>)))
  "Returns full string definition for message of type '<Gaze>"
  (cl:format cl:nil "float32 offset~%float32 distance~%float32 angle~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Gaze)))
  "Returns full string definition for message of type 'Gaze"
  (cl:format cl:nil "float32 offset~%float32 distance~%float32 angle~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Gaze>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Gaze>))
  "Converts a ROS message object to a list"
  (cl:list 'Gaze
    (cl:cons ':offset (offset msg))
    (cl:cons ':distance (distance msg))
    (cl:cons ':angle (angle msg))
))
